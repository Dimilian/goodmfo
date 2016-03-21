(function () {

    angular.module('django.csrf', []).config(function($httpProvider) {
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
});

    var calculator_app = angular.module('calc',['ui-rangeSlider','django.csrf']);


    calculator_app.controller('CalcCtrl', function($scope, $filter, $http){
        self=this;



        $scope.cases = function(current_term, words){
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



        $scope.summ = {
            'min': 5000,
            'max': 30000,
            'step':1000,
            'current':10000
        };

        $scope.term = {
            'min': 5,
            'max': 60,
            'step':1,
            'current':14,
            'words' : ["день","дней","дня"]
        };

        $scope.is_pensioner = false;

        //$('.ngrs-handle').mouseup(function(){
        //  self.calculate();
        //});


        this.payvar = function(payvar_id){
            $http.post('/getmoney/payvar/', {payvar: payvar_id}).then(
                function(answer){
                    $scope.payvar = answer.data;
                    $('.payvar_result').html($scope.payvar);
                    //console.log($scope.payvar);
                }
            )
        };

        this.calculate = function(){
          $http.post('/getmoney/calculate/', {amount: $scope.summ.current, days: $scope.term.current, is_pensioner: $scope.is_pensioner}).then(
              function(answer){
                  $scope.result = answer.data;
                  console.log($scope.result.rate);
                  $scope.rate = $scope.result.rate;
                  $scope.total = $scope.result.total;
                  $scope.program = $scope.result.title;
                  $scope.programNotFound = false;
              },
              function(reason){
                  console.log(reason);
                    if(reason.data.error == 'program_not_found'){
                        $scope.programNotFoundError = 'Программа не найдена!';
                        $scope.programNotFound = true;
                        $('.pay-variant').each(function(){
                            $(this).removeClass('pay-variant_active');
                        })
                    }
              }
          )
        };

        $('.block_calc-result').click(function(){
            console.log($scope.summ.current);
            self.calculate();
        })

        $('.pay-variant').click(function(){
            //console.log($(this).attr('id'))
            id = $(this).attr('id');
            $('.pay-variant').each(function(){
                $(this).removeClass('pay-variant_active');
            })
            $(this).siblings('.pay-variant').removeClass('pay-variant_active');
            $(this).addClass('pay-variant_active');
            self.payvar(id);
            switch (id){
                case ('contact'):
                    console.log('aui');
                case ('bank-balance'):
                    console.log('ui');
                    $('.payvar_result').show();
            }
        });

        $('#loan_submit').click(function(){
            console.log('loansubm');
            $http.post('/getmoney/loan_submit/', {program: $scope.program, rate:$scope.rate, summ:$scope.summ.current, term: $scope.term.current, result:$scope.total, payvar:$('.pay-variant_active').attr('id'), pens: $scope.is_pensioner}).then(
                function(answer){
                    $scope.payvar = answer.data;
                    //$('.payvar_result').html($scope.payvar);
                    console.log($scope.payvar);
                }
            )
        });

        $scope.$watchGroup(['summ.current','term.current'], function(newValues, oldValues){
            self.calculate();
        })

        $scope.$watch('is_pensioner', function(newValue, oldValue){
            if (newValue == true){
                $scope.summ.min = 5000;
                $scope.summ.max = 20000;
                $scope.summ.current = 10000;
                $scope.term.min = 20;
                $scope.term.max = 90;
                $scope.term.current = 30;
            } else {
                $scope.summ.min = 5000;
                $scope.summ.max = 30000;
                $scope.summ.current = 10000;
                $scope.term.current = 5;
                $scope.term.min = 5;
                $scope.term.max = 60;

            }
            console.log(oldValue);
            //self.calculate();
        //    $http({
        //          method: 'POST',
        //          url: '/ajax/calculate/',
        //          data: {}
        //        }).then(function successCallback(response) {
        //            console.log(response)
        //          }, function errorCallback(response) {
        //            console.log('net');
        //          });
        //    $scope.calcParams = newValues;
        //   self.findProduct(newValues[0], newValues[1]);
        //    //console.log(self.productCurrent.rate);
        //    //$scope.calcResultVar = self.calcResult(newValues[0], newValues[1], self.productCurrent.rate[0])
        });
    });

})();
$(function(){

    $(".button-collapse").sideNav();
    var link = window.location.pathname;
    link = link.substr(0, link.length -1);

    $('.side-nav li a[href="' + link + '"]').addClass('active');


    $(window).resize(function(){
        centerBlock();
    });
    // Для запуска функции при загрузке окна:
    $(window).resize();

    //центровка формы логина
    function centerBlock(){
        $('.login-form__wrap').css({
                               position:'absolute',
                               left: ($(window).width() - $('.login-form__wrap').outerWidth())/2,
                               top: ($(window).height() - $('.login-form__wrap').outerHeight())/2
                });
    }
});