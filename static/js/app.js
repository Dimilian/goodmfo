(function () {

    var calculator_app = angular.module('calc',['ui-rangeSlider']);


    calculator_app.controller('CalcCtrl', function($scope, $filter){
        self=this;

        this.cases = function(current_term, words){
                        var count = current_term % 100;
                        if ((count >= 5) && (count <= 20)) {
                            result = words[1];
                        } else {
                            count = count % 10;
                            if (count == 1) {
                                result = words[0];
                            } else if (count >=2 && count <= 4){
                                result = words[2];
                            } else {
                                result = words[1];
                            }
                        }
                        return result;
                    };

        this.products = [
            {'id':'0001', 'name':'Стандартный', 'rate':[1, 0.8]},
            {'id':'0002', 'name':'Пенсионный', 'rate':[0.7, 0.5]},
            {'id':'0003', 'name':'До зарплаты', 'rate':[1.2, 0.7]},
            {'id':'0004', 'name':'Минимальный платеж', 'rate':[1.5, 1.3]}
        ]

        this.summ = {
            'min': 5000,
            'max': 200000,
            'step':1000,
            'current':20000
        };

        this.term = {
            'min': 7,
            'max': 180,
            'step':1,
            'current':28,
            'words' : ["день","дней","дня"]
        };

        this.getProduct = function(products, id){
            var i = products.length;
            while (i--){
                if (products[i].id === id){
                    $scope.productCurrent = products[i];
                }

            }
        }
        this.findProduct = function(summ, term){
            $scope.errorBlock = false;
            if ((term >= 60 && summ >= 10000) || ( summ > 30000)){
				if (summ > 100000 && term <= 180){
					$scope.errorMessage = 'Для данной суммы необходим срок больше 180 дней!';
					$scope.errorBlock = true;
				} else if (summ > 30000 && term > 180){
					$scope.errorMessage = 'Для данной суммы необходим срок меньше 180 дней!';
					$scope.errorBlock = true;
				} else{
					id = '0001';
				}

			} else if ( term <= 28 && summ<=20000){
				id = '0003';
				$scope.errorMessage = '';
			} else if ( term >= 60 && summ <10000){
				$scope.errorMessage = 'Для данной суммы необходим срок меньше 60 дней!';
				$scope.errorBlock = true;
			} else if ((term <= 60 && summ >=5000) && (summ <= 30000)){
				id = '0004';
				$scope.errorMessage = '';
			} else{
				$scope.errorMessage = 'Для данной суммы необходим больший срок!';
				$scope.errorBlock = true;
			}

            if (!$scope.errorBlock){
                self.getProduct(self.products, id);
            }

        };

        this.calcResult = function(summ, term, rate){
            var result = (summ + (summ * (rate/100) * term));
            return result;
        }

        $scope.$watchGroup(['calc.summ.current', 'calc.term.current'], function(newValues){
            $scope.calcParams = newValues;
           self.findProduct(newValues[0], newValues[1]);
            //console.log(self.productCurrent.rate);
            //$scope.calcResultVar = self.calcResult(newValues[0], newValues[1], self.productCurrent.rate[0])
        });
    });

})();