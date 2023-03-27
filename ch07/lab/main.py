import rectangle
import surface

def main():
    r = rectangle(10, 10, 10, 10)
    assert((r.x, r.y, r.width, r.height) == (10, 10, 10, 10))
    r = rectangle(-1, 1, 1, 1)
    assert((r.x, r.y, r.width, r.height) == (1, 1, 1, 1))
    r = rectangle(1, -5, 1, 1)
    assert((r.x, r.y, r.width, r.height) == (1,5,1,1))
    r = rectangle(1, 1, -10, 1)
    assert((r.x, r.y, r.width, r.height) == (1,1,10,1))
    r = rectangle(1, 1, 1, -1000)
    assert((r.x, r.y, r.width, r.height) == (1,1,1,1000))

    s = surface("myimage.png", 10, 10, 10, 10)
    assert((s.rect.x, s.rect.y, s.rect.width, s.rect.height) == (10,10,10,10))
    srect = s.getRect()
    assert(srect.x,  s.getRect().y, srect.width,  srect.height) == (10,10,10,10)
    assert s.image
    print("Test Complete!")