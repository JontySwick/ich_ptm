# Тестовая коллекция в mongo atlas  sample_mflix.theaters
# Найти все кинотеатры в Калифорнии и посчитать их количество
use sample_mflix
db.theaters.countDocuments(
    {
        "location.address.state": 'CA'
    }
)

# Тестовая коллекция в mongo atlas  sample_airbnb.listingsAndReviews
# Найти недвижимость с самым большим количеством спален (bedrooms) и напишите ее название
use sample_airbnb
db.listingsAndReviews.find().sort({bedrooms: -1}).limit(1)

# Тестовая коллекция в mongo atlas  sample_airbnb.listingsAndReviews
# Найти недвижимость с самым высоким рейтингом  review_scores_rating при минимальном количестве отзывов 50 (number_of_reviews) и напишите ее название

db.listingsAndReviews.aggregate(
    [
        {
            $match: {
                number_of_reviews: {
                    $gte: 50
                }
            }
        },
        {
            $sort: {
                "review_scores.review_scores_rating": -1
            }
        },
        {
            $limit: 1
        }
    ]
)