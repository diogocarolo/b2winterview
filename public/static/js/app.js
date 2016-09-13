var app = angular.module('app', ['infinite-scroll']);

app.controller('tweets', ['$scope', '$http', function ($scope, $http) {
    $http.get("http://localhost:8080/tweets").success(function (data) {
    	$scope.tweets = data;
    	var page = 2;
		$scope.loadTweets = function() {
			$http.get("http://localhost:8080/moreTweets?page="+page).success(function (data) {
				for(var i = 0;i<data.length;i++){
					$scope.tweets.push(data[i]);
				}
			});
			page++;
		};
    });
}]);