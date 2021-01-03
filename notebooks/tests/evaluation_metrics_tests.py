def test_one(mod_arg):
    '''
    INPUT:
    mod_arg - a set of the strings pertaining to the objects that were passed in the fitting of our models

    OUTPUT:
    prints correctness of the set
    nothing returned
    '''
    a = 'X_train'
    b = 'X_test'
    c = 'y_train'
    d = 'y_test'
    e = 'training_data'
    f = 'testing_data'
    if mod_arg == {c, e}:
        print("That's right!  You need to fit on both parts of the data pertaining to training data!")
    else:
        print(
            "Oops!  That doesn't look quite right!  Remember you only want to fit your model to the training data!  Notice that X_train hasn't had the data cleaned yet, so that won't work to pass to our fit method. Hint - there are two items you should be passing to your fit method.")


def test_two(mod_arg):
    '''
    INPUT:
    model_arg - a set of the strings pertaining to the objects that were passed in the predicting step

    OUTPUT:
    prints correctness of the set
    nothing returned
    '''
    a = 'X_train'
    b = 'X_test'
    c = 'y_train'
    d = 'y_test'
    e = 'training_data'
    f = 'testing_data'
    if mod_arg == {f}:
        print(
            "That's right! To see how well our models perform in a new setting, you will want to predict on the test set of data.")
    else:
        print(
            "Oops!  That doesn't look quite right!  Remember you will want to predict on test data to know how well your model will do in a new situation.  Hint - there is only one item that should be passed to the predict method of your model.  Also notice that X_test has not been cleaned yet, so this cannot be passed to the predict method!")


def sol_seven(seven_sol):
    '''
    INPUT: dictionary with correct matching of metrics
    OUTPUT: nothing returned - prints statement related to correctness of dictionary
    '''

    a = "recall"
    b = "precision"
    c = "accuracy"
    d = 'f1-score'

    seven_sol_1 = {
        'We have imbalanced classes, which metric do we definitely not want to use?': c,
        'We really want to make sure the positive cases are all caught even if that means we identify some negatives as positives': a,
        'When we identify something as positive, we want to be sure it is truly positive': b,
        'We care equally about identifying positive and negative cases': d
    }

    if seven_sol == seven_sol_1:
        print(
            "That's right!  It isn't really necessary to memorize these in practice, but it is important to know they exist and know why might use one metric over another for a particular situation.")

    if seven_sol['We have imbalanced classes, which metric do we definitely not want to use?'] != seven_sol_1[
        'We have imbalanced classes, which metric do we definitely not want to use?']:
        print(
            "Oops!  The first one isn't right.  If we do not have balanced classes, we probably want to stay away from using accuracy.")

    if seven_sol[
        'We really want to make sure the positive cases are all caught even if that means we identify some negatives as positives'] != \
            seven_sol_1[
                'We really want to make sure the positive cases are all caught even if that means we identify some negatives as positives']:
        print(
            "Oops!  The second one isn't right.  If we really want to be sure about catching positive cases, we should be closely watching recall, which has all of the positive clases in the denominator - so we are monitoring how many of them we get right with recall.")

    if seven_sol['When we identify something as positive, we want to be sure it is truly positive'] != seven_sol_1[
        'When we identify something as positive, we want to be sure it is truly positive']:
        print(
            "Oops!  The third one isn't right.  Using precision, we have the predicted positives in the denominator.  Therefore, this will help us be sure the items we identify as positive are actually positive.")

    if seven_sol['We care equally about identifying positive and negative cases'] != seven_sol_1[
        'We care equally about identifying positive and negative cases']:
        print(
            "Oops!  The last one isn't right.  If we care equally about precision and recall, we should use f1 score.")


def sol_eight(eight_sol):
    '''
    INPUT: dictionary with correct matching of metrics
    OUTPUT: nothing returned - prints statement related to correctness of dictionary
    '''
    a = "naive-bayes"
    b = "bagging"
    c = "random-forest"
    d = 'ada-boost'
    e = "svm"

    eight_sol_1 = {
        'We have imbalanced classes, which metric do we definitely not want to use?': a,
        'We really want to make sure the positive cases are all caught even if that means we identify some negatives as positives': a,
        'When we identify something as positive, we want to be sure it is truly positive': c,
        'We care equally about identifying positive and negative cases': a
    }

    if eight_sol_1 == eight_sol:
        print("That's right!  Naive Bayes was the best model for all of our metrics except precision!")

    else:
        print(
            "Oops!  That doesn't look right.  Make sure you are performing your predictions and matching on the test data.  Hint: The naive bayes model actually performs best on all of the metrics except one.  Try again!")


def q1_check(models_dict):
    '''
    INPUT:
    models_dict - a dictionary with models and what types of problems the models can be used for

    OUTPUT:
    nothing returned
    prints statements related to the correctness of the dictionary
    '''
    a = 'regression'
    b = 'classification'
    c = 'both regression and classification'

    models = {
        'decision trees': c,
        'random forest': c,
        'adaptive boosting': c,
        'logistic regression': b,
        'linear regression': a,
    }

    if models == models_dict:
        print(
            "That's right!  All but logistic regression can be used for predicting numeric values.  And linear regression is the only one of these that you should not use for predicting categories.  Technically sklearn won't stop you from doing most of anything you want, but you probably want to treat cases in the way you found by answering this question!")

    if models['logistic regression'] != models_dict['logistic regression']:
        print("Oops!  In most cases, you will only want to use logistic regression for classification problems.")

    if models['linear regression'] != models_dict['linear regression']:
        print("Oops!  Linear regression should actually only be used in regression cases. Try again.")

    if (models['decision trees'] != models_dict['decision trees']) or (
            models['random forest'] != models_dict['random forest']) or (
            models['adaptive boosting'] != models_dict['adaptive boosting']):
        print(
            "Oops!  Actually random forests, decision trees, and adaptive boosting are all techniques that can be used for both regression and classification.  Try again!")


def q6_check(metrics):
    '''
    INPUT:
    metrics - a dictionary with metrics and what types of problems the metrics can be used for

    OUTPUT:
    nothing returned
    prints statements related to the correctness of the dictionary
    '''
    a = 'regression'
    b = 'classification'
    c = 'both regression and classification'

    #
    metrics_ch = {
        'precision': b,
        'recall': b,
        'accuracy': b,
        'r2_score': a,
        'mean_squared_error': a,
        'area_under_curve': b,
        'mean_absolute_area': a
    }

    if metrics_ch == metrics:
        print("That's right! Looks like you know your metrics!")

    if (metrics['precision'] != metrics['precision']) or (metrics['recall'] != metrics['recall']) or (
            metrics['accuracy'] != metrics['accuracy']) or (metrics['area_under_curve'] != metrics['area_under_curve']):
        print(
            "Oops!  Actually, there are four metrics that are used for classification.  Looks like you missed at least one of them.")

    if metrics != metrics_ch:
        print(
            "Oops!  Something doesn't look quite right.  You should have three metrics for regression, and the others should be for classification.  None of the metrics are used for both regression and classification.")


def check_ten(best_fit):
    '''
    INPUT:

    OUTPUT:

    '''
    a = 'decision tree'
    b = 'random forest'
    c = 'adaptive boosting'
    d = 'linear regression'

    best_fitting = {
        'mse': b,
        'r2': b,
        'mae': b
    }

    if best_fit == best_fitting:
        print("That's right!  The random forest was best in terms of all the metrics this time!")

    else:
        print(
            "Oops!  Actually the best model was the same for all the metrics.  Try again - all of your answers should be the same!")
