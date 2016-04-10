# TodoMVC - Backbone.js + Django

## Description

Create a REST API for use with the Backbone.js TodoMVC app.

## Normal Mode

Using the Django REST Framework, build an API with one resource: `todos`.

Your URLs should be nested under `/api/`, and will look like:

* GET `/api/todos/`
* POST `/api/todos/`
* PUT `/api/todos/{id}`
* DELETE `/api/todos/{id}`

The todo resource should have the following fields:

* id
* title - string, required
* completed - boolean, default false
* order - integer, not required, can be null

## Hard Mode

For hard mode, do everything shown above, plus add functional tests for your API.

## External Links
* [DRF Tutorial Requests and Reponses](http://www.django-rest-framework.org/tutorial/2-requests-and-responses/)
* [DRF Class based views](http://www.django-rest-framework.org/api-guide/views/)
* [DRF Serializers](http://www.django-rest-framework.org/api-guide/serializers/)
