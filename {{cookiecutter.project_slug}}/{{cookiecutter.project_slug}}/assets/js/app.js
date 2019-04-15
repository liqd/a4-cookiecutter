/* eslint no-unused-vars: "off", no-new: "off" */
/* global location */

// make jquery available for non-webpack js
var $ = window.jQuery = window.$ = require('jquery')

// load bootstrap components
require('bootstrap')

var django = require('django')

// expose react components
var ReactComments = require('adhocracy4').comments
var ReactRatings = require('adhocracy4').ratings
var ReactReports = require('adhocracy4').reports
var ReactFollows = require('adhocracy4').follows
{% if cookiecutter.add_polls_app == 'y' %}var ReactPolls = require('adhocracy4').polls{% endif %}
{% if cookiecutter.add_documents_app == 'y' %}var ReactDocuments = require('../../../apps/documents/assets/react_documents.jsx'){% endif %}

var initialiseWidget = function (namespace, name, fn) {
  var key = 'data-' + namespace + '-widget'
  var selector = '[' + key + '=' + name + ']'
  $(selector).each(function (i, el) {
    fn(el)

    // avoid double-initialisation
    el.removeAttribute(key)
  })
}

var init = function () {
  initialiseWidget('a4', 'comment', ReactComments.renderComment)
  initialiseWidget('a4', 'follows', ReactFollows.renderFollow)
  initialiseWidget('a4', 'ratings', ReactRatings.renderRatings)
  initialiseWidget('a4', 'reports', ReactReports.renderReports)
{% if cookiecutter.add_polls_app == 'y' %}  initialiseWidget('a4', 'polls', ReactPolls.renderPolls)
  initialiseWidget('a4', 'poll-management', ReactPolls.renderPollManagement){% endif %}
{% if cookiecutter.add_documents_app == 'y' %}  initialiseWidget('cc', 'document-management', ReactDocuments.renderDocumentManagement){% endif %}
}

$(init)
