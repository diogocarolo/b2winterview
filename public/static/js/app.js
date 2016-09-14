var app = angular.module('app', ['infinite-scroll']);

app.controller('tweets', ['$scope', '$http', function ($scope, $http) {
    $http.get("http://localhost:8080/tweets?page=1").success(function (data) {
    	$scope.tweets = data;
    	console.log($scope.tweets.length);
    	var page = 2;
    	$scope.busy = false;
		$scope.loadTweets = function() {
			if($scope.busy) {
				return;
			}
			$scope.busy = true;
			$http.get("http://localhost:8080/tweets?page="+page).success(function (data) {
				for(var i = 0;i<data.length;i++){
					$scope.tweets.push(data[i]);
				}
				$scope.busy = false;
			});
			page++;
		};
    });
}]);

app.controller('infoUser',['$scope','$http', function ($scope,$http) {
	$http.get("http://localhost:8080/infoUser").success(function (data) {
		$scope.infos = data;
		console.log($scope.infos);
	});
}]);