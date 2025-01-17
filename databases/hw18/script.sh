# Из коллекции sample_airbnb.listingsAndReviews найдите среднюю цену за сутки проживания на Гавайских островах.
use sample_airbnb
db.listingsAndReviews.aggregate(
    [
        {
            $match: {
                "address.location": {
                    $geoWithin: {
                        $centerSphere: [
                            [
                                -157.5599500536919,
                                20.683482423341385
                            ],
                            0.053455856249527416
                        ]
                    }
                }
            }
        },
        {
            $group: {
                _id: null,
                avgPrice: {
                    $avg: "$price"
                }
            }
        }
    ]
)

# 2.Подсчитайте в коллекции sample_mflix.movies, сколько фильмов имеют imdb рейтинг выше 8 и
# выходили в период с 2015 до 2023 года (используем year).
use sample_mflix
db.movies.countDocuments(
    {
        year: {
            $gte: 2015,
            $lte: 2023
        },
        "imdb.rating": {$gt: 8}
    }
)

# Какой из них имеет самый высокий рейтинг ?
db.movies.find(
    {
        year: {
            $gte: 2015,
            $lte: 2023
        },
        "imdb.rating": {$gt: 8}
    }
).sort({"imdb.rating": 1}).limit(1)