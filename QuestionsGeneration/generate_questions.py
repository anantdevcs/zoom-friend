from .pipelines import pipeline
import timeit

def gen_questions(text_list):
    '''
    Accepts a list of texts and generates ONE list of json questions and answers
    '''
    print('1')
    questions = []
    print('2')
    nlp = pipeline("e2e-qg")
    print('Pipeline loaded')
    for text in text_list:
        print('Generating the batch of results')
        print('3')
        res = nlp(text)
        print(res)
        questions += res
    return questions

if __name__ == '__main__':
    then = timeit.timeit()

    print(gen_questions(['aea']))
    now = timeit.timeit()

    print(f'Took {now - then} ')

    
