db.createUser({
  user: "valentin",
  pwd: "0000",
  roles: [{ role: "readWrite", db: "config" }],
});

db.clients.insertOne([
  {
    nom: "Mac Cain",
    prénom: "John",
    tel: 12345678,
  },
]);

db.clients.insertMany([
  {
    nom: "Massonniere",
    prénom: "Valentin",
    tel: 123456789,
  },
  {
    nom: "Dufour",
    prénom: "Alain",
    tel: 123456789,
    société: "Altran",
    niveau: 10,
  },
]);

db.clients.updateOne(
  { _id: ObjectId("68187429dadd1a6fb6b5f89a") },
  {
    $set: {
      société: "Microsoft",
    },
  }
);

db.clients.updateOne(
  { _id: ObjectId("681874c4dadd1a6fb6b5f89c") },
  {
    $unset: {
      niveau: 10,
    },
  }
);

db.clients.update(
  { _id: ObjectId("681874c4dadd1a6fb6b5f89c") },
  { $rename: { société: "company" } }
);

db.clients.find({}, { nom: 1, tel: 1, _id: 0 });
db.clients.find(
  {
    $or: [{ nom: "Mac Cain" }, { company: "Altran" }],
  },
  { nom: 1, prénom: 1, _id: 0 }
);

db.clients.find({}, { nom: 1, tel: 1, _id: 0 }).sort({ nom: 1 });
