## CKN network visualization

This is a small flask application which implements a visual browser of the [CKN network](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6130022/).

[vis.js](https://visjs.org/) is used for visualization and [selectize.js](https://selectize.dev/) is used for the search interface along with jquery, verge and Bootstrap.

**Please note that the backend and the search interface are only provisional as the code is intended to be integrated into a larger web application.**


### Requirements

-  docker
-  docker-compose


### How to run

The following command

```sh
$ docker-compose up --build
```

will build the images and run the container. The application is now available for testing at [http://localhost:5000](http://localhost:5000).


###  Authors

[Vid Podpečan](vid.podpecan@ijs.si)


### License

MIT
