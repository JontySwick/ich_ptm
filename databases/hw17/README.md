1. Тестовая коллекция в mongo atlas  sample_mflix.theaters
    
    Найти все кинотеатры в Калифорнии и посчитать их количество 


2. Тестовая коллекция в mongo atlas  sample_airbnb.listingsAndReviews

    Найти недвижимость с самым большим количеством спален (bedrooms) и напишите ее название 


3. Тестовая коллекция в mongo atlas  sample_airbnb.listingsAndReviews

    Найти недвижимость с самым высоким рейтингом  review_scores_rating при минимальном количестве отзывов 50 (number_of_reviews) и напишите ее название 

    ```json
    {
        filter: {
            number_of_reviews: {
                $gte: 50
            }
        },
        sort: {
            'review_scores.review_scores_rating': -1
        }
    }