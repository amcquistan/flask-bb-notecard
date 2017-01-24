var app = app || {};

app.CardView = Backbone.View.extend({
    tagName: 'a',
    className: 'list-group-item',
    initialize: function(opts){
        this.bus = opts.bus;
    },

    events: {
        'click': 'showCard'
    },

    showCard: function(){
        this.bus.trigger('cardSelected', this.model);
    },

    render: function(){
        this.$el.html(this.model.get('title'));
        return this;
    }
});


app.CardsView = Backbone.View.extend({
    
    initialize: function(opts) {
        this.bus = opts.bus;
        this.collection = opts.collection;
        this.listenTo(this.collection, 'add', this.render);
        this.render();
    },

    render: function(){
        var self = this;
        self.collection.each(function(card){
            var view = new app.CardView({ model: card, bus: self.bus });
            self.$el.append(view.render().$el);
        });
        
        return self;
    }
});

app.ShowCardView = Backbone.View.extend({

    template: _.template($('#show-card-tmpl').html()),

    initialize: function(opts){
        this.bus = opts.bus;
        
        this.bus.on('cardSelected', this.cardSelected, this);
        this.render();
    },

    events: {
        'click .show-hide': 'toggleAnswer'
    },

    toggleAnswer: function(evt){
        this.$('.show-hide').toggle();
        this.$('#card-answer').toggle();
        evt.preventDefault();
    },

    cardSelected: function(card){
        this.model = card;
        this.render();
    },

    render: function(){
        if(this.model){
            // this.$el.html(this.model.get('name'));
            this.$el.html(this.template(this.model.attributes));
        }

        return this;
    }
});

