How the questions data structure should look like after getting the data from the api:
keys                values
response            int         // specifies the return value of the request
category            string      // specifies the questions category
difficulty          string      // specifies the difficulty of the question
question            string      // the question to be asked
correct answer      string      // the correct answer to the question
answers             list[string] // all answers to the question

difficulty can be easy, medium and hard when sending a request to the api it can also be any
but the return from the api will be easy medium or hard
