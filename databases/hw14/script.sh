use ich
# Из коллекции customers выяснить из какого города "Sven Ottlieb"
db.customers.find({ContactName: "Sven Ottlieb"}, {_id: 0, City: 1})

# Из коллекции ich.US_Adult_Income найти возраст самого взрослого человека
db.US_Adult_Income.find({age: {$gt: 0}}, {age: 1, _id: 0}).sort({age: -1}).limit(1)

# Из 2 задачи выясните, сколько человек имеют такой же возраст
db.US_Adult_Income.countDocuments({age: 90})

# Найти _id ObjectId документа, в котором education " IT-career-hub"
db.US_Adult_Income.find({education: " IT-career-hub"}, {_id:1})

# Выяснить количество людей в возрасте между 20 и 30 годами
db.US_Adult_Income.countDocuments({age: {$lt: 30, $gt: 20}})