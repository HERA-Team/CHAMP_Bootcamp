import numpy as np

def perp(a):
    b = np.empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b

def intersection(a1,a2, b1,b2):
    a1.shape = (-1,1)
    a2.shape = (-1,1)
    if len(b1.shape) < 2:
        b1.shape = (-1,1)
        b2.shape = (-1,1)
    da,db,dp = a2-a1, b2-b1, a1-b1
    dap = perp(da)
    denom = np.dot(dap.T, db).astype(np.float)
    num = np.dot(dap.T, dp)
    return (num / denom)*db + b1

def intersects(a1,a2,b1,b2):
    ints = intersection(a1,a2,b1,b2)
    minbx = np.where(b1[0] < b2[0], b1[0], b2[0])
    maxbx = np.where(b1[0] > b2[0], b1[0], b2[0])
    minby = np.where(b1[1] < b2[1], b1[1], b2[1])
    maxby = np.where(b1[1] > b2[1], b1[1], b2[1])
    minax = np.where(a1[0] < a2[0], a1[0], a2[0])
    maxax = np.where(a1[0] > a2[0], a1[0], a2[0])
    minay = np.where(a1[1] < a2[1], a1[1], a2[1])
    maxay = np.where(a1[1] > a2[1], a1[1], a2[1])
    bxok = np.logical_and(ints[0] >= minbx, ints[0] <= maxbx)
    byok = np.logical_and(ints[1] >= minby, ints[1] <= maxby)
    axok = np.logical_and(ints[0] >= minax, ints[0] <= maxax)
    ayok = np.logical_and(ints[1] >= minay, ints[1] <= maxay)
    bok = np.logical_and(bxok, byok)
    aok = np.logical_and(axok, ayok)
    return np.logical_and(bok, aok)

if __name__ == '__main__':

    import pylab as plt
    #p1s = np.array([
    #    [0., 0.],
    #    [4.,-5.],
    #    [2., 2.],
    #    [6., 0.],
    #    [2., 3.],
    #]).transpose()

    #p2s = np.array([
    #    [1., 0.],
    #    [4., 2.],
    #    [4., 3.],
    #    [6., 3.],
    #    [5., 0.],
    #]).transpose()
    curpos = np.array([ 0.45304585,  0.54069817])
    newpos = np.array([ 0.35333599, 0.54831025])
    p1 = np.array([0,1])
    p2 = np.array([0,0])
    plt.plot([curpos[0],newpos[0]],[curpos[1],newpos[1]])
    plt.plot([p1[0],p2[0]],[p1[1],p2[1]])

    print intersects(curpos,newpos,p1,p2)
    #for x1,y1,x2,y2 in zip(p1s[0],p1s[1],p2s[0],p2s[1]):
    #    plt.plot([x1,x2],[y1,y2])
    plt.show()
    print intersects(p1s[:,0],p2s[:,0], p1s, p2s)
    print intersects(p1s[:,-1],p2s[:,-1], p1s, p2s)

