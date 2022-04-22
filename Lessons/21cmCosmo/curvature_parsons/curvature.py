import pygame as pg, numpy as np
import sys
#import intersect
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL.Image import open

def dist(pos1, pos2):
    dpos = pos1-pos2
    return np.sqrt(dpos[0]**2 + dpos[1]**2 + dpos[2]**2)

def rot_m(ang, vec):
    c = np.cos(ang); s = np.sin(ang); C = 1-c
    x,y,z = vec[...,0], vec[...,1], vec[...,2]
    xs,ys,zs = x*s, y*s, z*s
    xC,yC,zC = x*C, y*C, z*C
    xyC,yzC,zxC = x*yC, y*zC, z*xC
    rm = np.array([[x*xC+c, xyC-zs, zxC+ys],
                   [xyC+zs, y*yC+c, yzC-xs],
                   [zxC-ys, yzC+xs, z*zC+c]], dtype=np.double)
    axes = range(rm.ndim)
    return rm.transpose(axes[-1:] + axes[:-1])

class Camera:
    def __init__(self, pos=np.array([0.,0,0]), ang=0.):
        self.pos = pos
        self.ang = ang
    def turn(self, dang):
        curpos = self.pos.copy()
        self.move(-curpos)
        glRotatef(dang*180/np.pi,0,1,0)
        self.move(curpos)
        self.ang += dang
    def move(self, dpos):
        glTranslatef(dpos[0],dpos[2], dpos[1])
        self.pos += dpos
    def get_heading(self):
        return np.array([-np.sin(self.ang), np.cos(self.ang), 0])

class Cube:
    def __init__(self, pos=np.array([2.,2,0]), side=.5):
        self.pos = pos
        self.side = side
        self.spin = 0.
        self.twist = 0.
    def get_vertices(self, pos, side):
        c = np.array([pos[0], pos[2], pos[1]]); c.shape = (1,-1)
        u = side/2
        v = np.array([(u,-u,-u), (u,u,-u), (-u,u,-u), (-u,-u,-u), (u,-u,u), (u,u,u), (-u,-u,u), (-u,u,u)])
        m1 = rot_m(self.spin, np.array([1,0,0]))
        m2 = rot_m(self.twist, np.array([0,0,1]))
        v = np.dot(m1, np.dot(m2, v.T)).T
        return v + c
    def get_sides(self):
        return ((0,1,2,3), (6,7,5,4), (4,5,1,0), (3,2,7,6), (6,4,0,3), (2,1,5,7))
    def get_colors(self):
        return self.get_vertices(np.array([0.,0,0]),1.)+.5
    def draw_sides(self, campos, rfunc):
        r = self.pos - campos
        d = np.sqrt(np.dot(r,r))
        r /= d
        rscalar = rfunc(d)
        _c = np.array([campos[0], campos[2], campos[1]])
        _r = np.array([r[0], r[2], r[1]])
        sides = self.get_sides()
        verts = self.get_vertices(self.pos-campos, self.side)
        _c.shape = (1,3)
        prj = np.dot(verts,_r)
        prj.shape = (-1,1)
        _r.shape = (1,3)
        verts = (verts - prj * _r) / rscalar + prj * _r
        verts += _c
        colors = self.get_colors()
        glEnable(GL_BLEND)
        glPushAttrib(GL_CURRENT_BIT) # save current color
        glBegin(GL_QUADS)
        for i0,i1,i2,i3 in sides:
            glColor3f(*colors[i0]); glVertex3f(*verts[i0])
            glColor3f(*colors[i1]); glVertex3f(*verts[i1])
            glColor3f(*colors[i2]); glVertex3f(*verts[i2])
            glColor3f(*colors[i3]); glVertex3f(*verts[i3])
        glEnd()
        glPopAttrib() # restore current color
        self.twist += .01
        self.spin += .02

def loadImage(filename):
    """Load an image file as a 2D texture using PIL"""
    im = open(filename).convert("RGBA")
    ix, iy, image = im.size[0], im.size[1], im.tobytes("raw", "RGBA", 0, -1)
    ID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, ID)
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    return ID

class Wall:
    def __init__(self, spos, epos, texid, hgt=1., hoff=-.5):
        self.spos,self.epos = spos, epos
        self.hgt = hgt
        self.hoff = hoff
        self.verts = ((spos[0],    hoff,spos[1]),
                      (epos[0],    hoff,epos[1]),
                      (epos[0],hgt+hoff,epos[1]),
                      (spos[0],hgt+hoff,spos[1]))
        self.texid = texid
    def setup_drawing(self, interp=GL_NEAREST, transp=GL_ONE_MINUS_SRC_ALPHA):
        '''interp=GL_NEAREST,GL_LINEAR
        transp=GL_ONE,GL_ONE_MINUS_SRC_ALPHA'''
        glBindTexture(GL_TEXTURE_2D, self.texid)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, interp)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, interp)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
        glBlendFunc(GL_SRC_ALPHA, transp)
        glEnable(GL_BLEND)
        glEnable(GL_TEXTURE_2D)
        glBegin(GL_QUADS)
    def render(self, campos, rfunc):
        pos = 0.5*np.array([self.spos[0]+self.epos[0], self.spos[1]+self.epos[1], 0])
        r = pos - campos
        d = np.sqrt(np.dot(r,r))
        r /= d
        rscalar = rfunc(d)
        _c = np.array([campos[0], campos[2], campos[1]])
        _r = np.array([r[0], r[2], r[1]])
        verts = np.array(list(self.verts))
        _c.shape = (1,3)
        prj = np.dot(verts,_r)
        prj.shape = (-1,1)
        _r.shape = (1,3)
        verts = (verts - prj * _r) / rscalar + prj * _r
        #verts += _c
        glTexCoord2f(0.,0.); glVertex3fv(verts[0])
        glTexCoord2f(1.,0.); glVertex3fv(verts[1])
        glTexCoord2f(1.,1.); glVertex3fv(verts[2])
        glTexCoord2f(0.,1.); glVertex3fv(verts[3])
    def teardown_drawing(self):
        glEnd()
        glDisable(GL_BLEND)
        glDisable(GL_TEXTURE_2D)
    def draw(self, campos, rfunc):
        self.setup_drawing()
        self.render(campos, rfunc)
        self.teardown_drawing()

class Maze:
    def __init__(self, maze_rep=None, texid=None, hgt=1, hoff=-.5):
        if maze_rep != None:
            self.img = self.from_file(maze_rep)
            pos_list = self.from_img(self.img)
            self.walls = [Wall(p[0],p[1], texid, hgt=hgt, hoff=hoff) for p in pos_list]
            self.lines = np.array(pos_list)
        else:
            self.walls = []
            self.lines = []
    def is_wall(self, pos):
        if self.img[pos[0],pos[1]] == 0: return False
        return True
    def from_file(self, filename):
        f = open(filename)
        d = np.array(f.getdata())
        d = d[:,0]**2 + d[:,1]**2 + d[:,2]**2
        if False:
            d.shape = (f.size[0]/2,2,f.size[1]/2,2)
            d = np.average(d, axis=3)
            d = np.average(d, axis=1)
        else:
            d.shape = (f.size[0],f.size[1])
        d = np.where(d > d.max()/2, 0, 1)
        return d
    #def intersects(self, curpos, newpos, clip=True):
    #    if not clip: return False
    #    p1 = self.lines[:,0,:].T
    #    p2 = self.lines[:,1,:].T
    #    return np.any(intersect.intersects(-curpos, -newpos, p1, p2))
    def from_img(self, img):
        dx = img[1:] - img[:-1]
        inds = np.where(dx != 0)
        x,y = np.indices(dx.shape)
        dx_x,dx_y = x[inds].flatten(), y[inds].flatten()
        pos_list = []
        for x,y in zip(dx_x, dx_y):
            pos_list.append([np.array([x+.5,y+.5]), np.array([x+.5,y-.5])])
        dy = img[:,1:] - img[:,:-1]
        inds = np.where(dy != 0)
        x,y = np.indices(dy.shape)
        dy_x,dy_y = x[inds].flatten(), y[inds].flatten()
        for x,y in zip(dy_x, dy_y):
            pos_list.append([np.array([x+.5,y+.5]), np.array([x-.5,y+.5])])
        return pos_list
    def draw_walls(self, curpos, rfunc, rmax=50.):
        self.walls[0].setup_drawing()
        for i,w in enumerate(self.walls):
            #if (self.lines[i,0,0]-curpos[0])**2 + (self.lines[i,0,1]-curpos[1])**2 > rmax**2: continue
            w.render(curpos, rfunc)
        self.walls[0].teardown_drawing()
    def draw_background(self, display, interp=GL_NEAREST):
        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        return
    def fog(self):
        glEnable(GL_FOG)                        # Enable fog
        glFogi(GL_FOG_MODE, GL_LINEAR)          # Set fog settings
        glFogfv(GL_FOG_COLOR, (1., 0., 0., 1.))   # Set fog color
        glFogf(GL_FOG_DENSITY, 0.15)            # Set fog density
        glHint(GL_FOG_HINT, GL_DONT_CARE)       # Set Hint
        glFogf(GL_FOG_START, 2.0);              # Fog start 
        glFogf(GL_FOG_END, 30.0);                # Fog end
        
        
STEP = .2
def main():
    pg.init()
    display = (400,300)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)

    #glClearColor(1.0, 1.0, 1.0, 0.0)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_NORMALIZE)
    glEnable(GL_COLOR_MATERIAL) 
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    gluPerspective(45, (float(display[0])/display[1]), 0.1, 50.0)

    galaxy_id  = loadImage('art/galaxy.png')

    maze = Maze()
    if True: # Add galaxies to the universe
        for i in xrange(0,10,3):
            for j in xrange(0,10,3):
                w = Wall([i,j], [i+1,j], galaxy_id)
                maze.walls.append(w)

    cubes = []
    if False: # Add spinning cubes to the universe
        for i in xrange(0,10,3):
            for j in xrange(0,10,3):
                cubes.append(Cube(np.array([i,j,0])))
    # Initial positions
    cam = Camera()
    cam.turn(3.75*np.pi)
    cam.move(np.array([-0.75,-0.5,0]))

    R = 10. # radius of curvature of the universe

    def rfunc(d):
        '''Map the actual distance to the effective ang diameter distance.'''
        if sys.argv[-1] == 'closed': return R * np.sin(d/R) / d # closed
        elif sys.argv[-1] == 'open': return R * np.sinh(d/R) / d # open
        else: return 1. # flat

    while True:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit(); quit()
        maze.draw_background(display)
        maze.fog() # draw the reddening; comment out for none
        maze.draw_walls(-cam.pos, rfunc)
        for cube in cubes:
            cube.draw_sides(-cam.pos, rfunc)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            cam.turn(-.03)
            print cam.ang, cam.pos
        if keys[pg.K_RIGHT]:
            cam.turn(.03)
            print cam.ang, cam.pos
        if keys[pg.K_UP]:
            h = cam.get_heading()
            curpos = cam.pos.copy()
            newpos = cam.pos + 2*STEP*h
            cam.move(STEP*h)
            print cam.ang, cam.pos
        if keys[pg.K_DOWN]:
            h = cam.get_heading()
            curpos = cam.pos.copy()
            newpos = cam.pos - 2*STEP*h
            cam.move(-STEP*h)
            print cam.ang, cam.pos
        pg.display.flip()
        pg.time.wait(10)


main()
