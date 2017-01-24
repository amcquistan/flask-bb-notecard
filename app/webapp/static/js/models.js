
var app = app || {};

app.Subject = Backbone.Model.extend({});
app.Subjects = Backbone.Collection.extend({
    model: app.Subject
});

app.Card = Backbone.Model.extend({});
app.Cards = Backbone.Collection.extend({
    model: app.Card
});
