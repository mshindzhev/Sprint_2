class PointsForPlace:
    points = 0

    @classmethod
    def get_points_for_place(cls, place):
        if place > 100:
            print(f'Спортсмен не может занять нулевое или отрицательное место')
        elif place < 1:
            print(f'Спортсмен не может занять нулевое или отрицательное место')
        else:
            PointsForPlace.points = 101 - place
            return PointsForPlace.points


class PointsForMeters:
    points = 0

    @classmethod
    def get_points_for_meters(cls, meters):
        if meters < 0:
            print(f'Количество метров не может быть отрицательным')
        else:
            PointsForMeters.points = int(meters * 0.5)
            return PointsForMeters.points

class TotalPoints(PointsForPlace, PointsForMeters):
    total = 0

    @classmethod
    def get_total_points(cls, place, meter):
        TotalPoints.total = PointsForPlace.get_points_for_place(place) + PointsForMeters.get_points_for_meters(meter)
        return TotalPoints.total

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))