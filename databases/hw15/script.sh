# Коллекция imdb : Используя оператор $size, найдите фильмы, написанные 3 сценаристами (writers) и снятые 2 режиссерами (directors)
use ich
db.imdb.find({
  writers: {$size: 3}
  directors: {$size: 2},
})
# Коллекция bookings: Найдите адрес нахождения автомобиля с vin WME4530421Y135045 по самой последней дате (и времени) final_date
db.bookings.find({
  vin: 'WME4530421Y135045'
}).projection({
  init_date: 1
}).sort({
  final_date: -1,
  final_time: -1
}).limit(1)

# Коллекция bookings: подсчитайте, у скольких автомобилей при окончании аренды закончилось топливо (final_fuel)
db.bookings.countDocuments({
  final_fuel: 0
})

# Коллекция bookings: найдите номерной знак и vin номер авто, с самым большим километражом (distance)
db.bookings.find().projection({
  _id:0,
  vin: 1,
  plate: 1
}).sort({
  distance: -1
}).limit(1)

# Коллекция imdb. Найдите фильм с участием "Brad Pitt" с самым высоким рейтингом (imdb.rating)
db.imdb.find({
  cast: "Brad Pitt",
  'imdb.rating': {$ne: ""}
}).sort({'imdb.rating': -1}).limit(1)