var app = angular.module('app', []);

app.controller('tweets', ['$scope', '$http', function ($scope, $http) {
    $http.get("http://localhost:8080/tweets").success(function (data) {
    	$scope.text = data;
    });
}]);