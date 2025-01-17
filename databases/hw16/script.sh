# Найдите средний возраст из коллекции ich.US_Adult_Income
use ich
db.US_Adult_Income.aggregate(
    {
        $group: {
            _id: null,
            avgAge: {
                $avg: "$age"
            }
        }
    }
)

# Поменяв подключение к базе данных, создать коллекцию orders_NAME (для уникальности - добавим ваше имя в название)
# со свойствами id, customer, product, amount, city, используя следующие данные:
#    1 Olga Apple 15.55 Berlin
#    2 Anna Apple 10.05 Madrid
#    3 Olga Kiwi 9.6 Berlin
#    4 Anton Apple 20 Roma
#    5 Olga Banana 8 Madrid
#    6 Petr Orange 18.3 Paris
db.createCollection(
    'orders_kirill',
    {
        validator: {
            $jsonSchema: {
                bsonType: 'object',
                required: ['id', 'customer', 'product', 'amount', 'city'],
                properties: {
                    id: {
                        bsonType: 'int',
                        minimum: 1,
                        description: 'id mast be unique and 1 or greater'
                    },
                    customer: {
                        bsonType: 'string',
                        description: 'Customer must be str type'
                    },
                    product: {
                        bsonType: 'string',
                        description: 'Product must be str type'
                    },
                    amount: {
                        bsonType: ['int', 'double'],
                        minimum: 0,
                        description: 'amount must be int or double type and greater that 0'
                    },
                    city: {
                        bsonType: 'string',
                        description: 'City must be str type'
                    }

                }
            }
        },
        validationLevel: 'strict',
        validationAction: 'error'
    }
)

db.orders_kirill.createIndex(
    {id: 1}, {unique: true}
)

db.orders_kirill.insertMany(
    [
        {
            id: 1,
            customer: 'Olga',
            product: 'Apple',
            amount: 15.55,
            city: 'Berlin'
        },
        {
            id: 2,
            customer: 'Anna',
            product: 'Apple',
            amount: 10.05,
            city: 'Madrid'
        },
        {
            id: 3,
            customer: 'Olga',
            product: 'Kiwi',
            amount: 9.6,
            city: 'Berlin'
        },
        {
            id: 4,
            customer: 'Anton',
            product: 'Apple',
            amount: 20,
            city: 'Roma'
        },
        {
            id: 5,
            customer: 'Olga',
            product: 'Banana',
            amount: 8,
            city: 'Madrid'
        },
        {
            id: 6,
            customer: 'Petr',
            product: 'Orange',
            amount: 18.3,
            city: 'Paris'
        }
    ]
)

# Найти сколько всего было совершено покупок
db.orders_kirill.countDocuments()

# Найти сколько всего раз были куплены яблоки
db.orders_kirill.countDocuments(
    {
        product: 'Apple'
    }
)

# Вывести идентификаторы трех самые дорогих покупок
db.orders_kirill.find().sort({amount: -1}).limit(3)

# Найти сколько всего покупок было совершено в Берлине // 2
db.orders_kirill.countDocuments(
    {
        city: 'Berlin'
    }
)


#  Найти количество покупок яблок в городах Берлин и Мадрид // 2
db.orders_kirill.countDocuments(
    {
        $and: [
            {product: 'Apple'},
            {$or: [ {city: 'Berlin'}, {city: 'Madrid'} ]}
        ]
    }
)

# Найти сколько было потрачено каждым покупателем
db.orders_kirill.aggregate(
    {
        $group: {
            _id: '$customer',
            total: {$sum: '$amount'}
        }
    }
)

# Найти в каких городах совершала покупки Ольга
db.orders_kirill.aggregate(
    [{
        $match: {
            customer: 'Olga'
        }
    },
    {
       $group:{
           _id: '$city'
       }
    }]
)