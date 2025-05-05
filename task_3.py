class PointsForPlace:

    def __init__(self):
        self.points = 0

    def get_points_for_place(self, place):
        if place > 100:
            print(f'Спортсмен не может занять нулевое или отрицательное место')
        elif place < 1:
            print(f'Спортсмен не может занять нулевое или отрицательное место')
        else:
            self.points = 101 - place
            return self.points


class PointsForMeters:

    def __init__(self):
        self.points = 0

    def get_points_for_meters(self, meters):
        if meters < 0:
            print(f'Количество метров не может быть отрицательным')
        else:
            self.points = int(meters * 0.5)
            return self.points

class TotalPoints(PointsForPlace, PointsForMeters):

    def get_total_points(self, place, meter):
        total = self.get_points_for_place(place) + self.get_points_for_meters(meter)
        return total

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))