var moviedb = [{
        title: "In Bruges",
        rating: 5,
        watched: true
    },
    {
        title: "Mad Max Fury Road",
        rating: 5,
        watched: false
    },
    {
        title: "Frozen",
        rating: 3,
        watched: false
    },
    {
        title: "Les Miserables",
        rating: 2.5,
        watched: true
    },
];

moviedb.forEach(function (movie) {
    let watched = " ";
    if (!movie.watched) {
        watched = " not ";
    }
    console.log("You have" + watched + "seen " + "\"" + movie.title + "\"" + " - " + movie.rating + " stars.");
});