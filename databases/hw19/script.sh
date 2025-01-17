# Из базы данных ich работаем с коллекцией ich.Spotify_Youtube:
use ich

# Найдите трек с наивысшими показателями  Danceability и Energy.
db.Spotify_Youtube.aggregate(
    [
        {
            $match:

                {
                    Danceability: {
                        $exists: true
                    },
                    Energy: {
                        $exists: true
                    }
                }
        },
        {
            $project:

                {
                    danceAndEnergy: {
                        $add: ["$Danceability", "$Energy"]
                    },
                    Artist: 1,
                    Track: 1,
                    Album: 1
                }
        },
        {
            $sort:

                {
                    danceAndEnergy: -1
                }
        },
        {
            $limit: 1
        }
    ]
)

# У какого трека (но не compilation) самая большая длительность?
db.Spotify_Youtube.find(
    {
        Album_type: {$ne: 'compilation'}
    }
).sort({Duration_ms: -1}).limit(1)


# В каком одном альбоме самое большее количество треков?
db.Spotify_Youtube.aggregate(
    [
        {
            $group:

                {
                    _id: "$Album",
                    treak_qty: {
                        $sum: 1
                    }
                }
        },
        {
            $sort: {
                treak_qty: -1
            }
        },
        {
            $limit: 1
        }
    ]
)

# Сколько просмотров видео на youtube у трека с самым высоким количеством прослушиваний на spotify (Stream)?
db.Spotify_Youtube.find(
    {
        Url_youtube: {$exists: true},
    }
).sort({Stream: -1}).limit(1).projection(
    {Views: 1, _id: 0, Track: 1, Artist: 1}
)

# Экспортируйте 20 самых популярных (прослушивания или просмотры) трек
db.Spotify_Youtube.aggregate(
    [
        {
            $sort: {
                Stream: -1
            }
        },
        {$limit: 20},
        {
            $out:
                {
                    db: "Examle",
                    coll: "example1"
                }
        }
    ]
)