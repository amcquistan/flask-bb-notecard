
var app = app || {};

// event busses (aggregated) used to link multiple views, collections, and models
 
// app.subjectEvtBus = _.extend({}, Backbone.Events);

app.SubjectView = Backbone.View.extend({
    events: {
        'click .subject-edit-lnk': 'editSubject',
        'click .subject-save-edit': 'saveEdit',
        'click .subject-cancel-edit': 'cancelEdit'
    },
	template: _.template($('#subjectTmpl').html()),
	render: function(){
		this.$el.html(this.template(this.model.toJSON()));
		return this;
    },
    editSubject: function(evt){
        this.template = _.template($('#subjectEditTmpl').html());
        this.render();
        evt.preventDefault();
    },
    saveEdit: function(evt){
        var form = this.$el.find('div#edit-input-div');
        this.model.set({
            name: form.find('input#name').val(),
            description: form.find('textarea#description').val()
        });
        this.model.save();
        evt.preventDefault();
    },
    cancelEdit: function(evt){
        template = _.template($('#subjectTmpl').html());
        this.render();
    }
});


app.SubjectsView = Backbone.View.extend({
    initialize: function(opts){
        var opts = opts || {};
        this.collection = opts.collection;
        this.listenTo(this.collection, 'add', this.render);
        this.listenTo(this.collection, 'change', this.render);
    },
    events:{
        'click #new-subject': 'showNewForm',
        'click #subject-save-new': 'saveNew',
        'click #subject-cancel-new': 'cancelNew'
    },
    newTemplate: _.template($('#subjectNewTmpl').html()),
	render: function(){
		var self = this;
        self.$('#subjects').empty();
        self.collection.each(function(subject) {
			var view = new app.SubjectView({model: subject});
            self.$('#subjects').append(view.render().$el);
        });
    },
    showNewForm: function(evt) {
        this.$('#subjects').prepend(this.newTemplate({}));
        evt.preventDefault();
    },
    cancelNew: function(evt) {
        evt.preventDefault();
        console.log('Clicked cancle new btn');
        this.render();
    },
    saveNew: function(evt){
        var self = this;
        var form = self.$el.find('div#new-input-div');
        var subject = new app.Subject();
        subject.set({
            name: form.find('input#name').val(),
            description: form.find('textarea#description').val()
        });
        subject.url = self.collection.url;
        subject.save().then(
            function(response){
                console.log(response);
                console.log('success!');
                self.collection.add(subject);
            },
            function(error){
                console.log(error);
                console.log('there was an error');
            }
        );
        evt.preventDefault();
    }
});

