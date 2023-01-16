from graphics import *

class Snake:
    def __init__(self, x, y, length, direction):
        self.x = x
        self.y = y
        self.length = length
        self.direction = direction
        self.body = list()
        seg = Segment(self.x, self.y, self.direction, lifetime = self.length, ishead = True)
        self.body.append(seg)

    def _key_to_direction(self, key):
        if key == "Up":
            return 0
        elif key == "Down":
            return 2
        elif key == "Left":
            return 3
        elif key == "Right":
            return 1
        else:
            return self.direction

    def move(self, key):
        self.update()
        dir = self._key_to_direction(key)
        # 今のdirectionと差が2以上なら、directionを変えない
        # ただし0と3の場合は例外
        if abs(self.direction - dir) >= 2 and not (self.direction == 0 and dir == 3) and not (self.direction == 3 and dir == 0):
            dir = self.direction
        self.direction = dir
        # 次のsegmentの位置を計算
        if self.direction == 0:
            self.y += 20
        elif self.direction == 1:
            self.x += 20
        elif self.direction == 2:
            self.y -= 20
        elif self.direction == 3:
            self.x -= 20
        # コリジョン判定
        if self.coliision():
            # 例外を投げる
            raise Exception("Game Over")
        # bodyの先頭に新しいSegmentを追加
        self.body.insert(0, Segment(self.x, self.y, direction = self.direction, lifetime = self.length, ishead = True))
    
    def coliision(self):
        # 画面外に出たら
        if self.x < 100 or self.x > 500 or self.y < 100 or self.y > 500:
            return True
        # 自分の体にぶつかったら
        for segment in self.body:
            if segment.x == self.x and segment.y == self.y:
                return True
        return False

    def draw(self, window):
        # 再描画
        for segment in self.body:
            segment.draw(window)

    def eat(self):
        self.length += 1

    def update(self):
        for segment in self.body:
            seg = segment.update()
            if seg is not None:
                self.body.remove(segment)

class Segment:
    def __init__(self, x, y, direction, lifetime, ishead=True):
        self.x = x
        self.y = y
        self.direction = direction
        self.ishead = ishead
        self.lifetime = lifetime
        self.isdraw = False
        self.body = None

    def draw(self, window):
        if self.isdraw == False:
            if self.ishead:
                self.body = Circle(Point(self.x, self.y), 10)
                self.body.setFill("orange")
            else:
                self.body.undraw()
                self.body.setFill("green")
                self.isdraw = True
            self.body.draw(window)

    def update(self):
        if self.ishead:
            self.ishead = False
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.body.undraw()
            return self.body
        else:
            return None

    def getlifetime(self):
        return self.lifetime
    
    def setlifetime(self, lifetime):
        self.lifetime = lifetime