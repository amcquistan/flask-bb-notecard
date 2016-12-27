
var app = app || {};

app.SubjectView = Backbone.View.extend({
	template: _.template($('#subjectTmpl').html()),
	render: function(){
		this.$el.html(this.template(this.model.toJSON()));
		return this;
    }
});

app.SubjectsView = Backbone.View.extend({
    initialize: function(){
        this.listenTo(this.collection, 'add', this.render);
    },
	render: function(){
		var self = this;
        self.$el.empty();
		self.collection.each(function(subject) {
			var view = new app.SubjectView({model: subject});
			self.$el.append(view.render().$el);
        })
    }
});
