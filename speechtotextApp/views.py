from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.utilities import SQLDatabase
import sqlalchemy
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from sqlalchemy.exc import ProgrammingError
from django.http import JsonResponse
from django.shortcuts import render

pg_connect_uri = f'postgresql://postgres:root@localhost:5432/3969_HW1_Q3'
db = SQLDatabase.from_uri(pg_connect_uri)
def get_schema(_):
    #print("get_schema input: ",db)
    #nonlocal db
    schema = db.get_table_info()
    return schema


def chat_view(request):
    return render(request, 'speechtotextApp/index.html')

class GeeksCreate(CreateView):

    def get(self, request, *args, **kwargs):
       

        API_KEY = ""
        # engine = sqlalchemy.create_engine(pg_connect_uri)

        # with engine.connect() as conn:
        #     result = conn.execute(sqlalchemy.text("select * from movie limit 10"))
        #     META_DATA = sqlalchemy.MetaData(bind=conn, reflect=True)
        # print("Done")

        template = """Based on the table schema below, write a SQL query that would answer the user's question:
        {schema}

        Question: {question}
        SQL Query:"""
        prompt = ChatPromptTemplate.from_template(template)

        llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0, api_key=API_KEY)

        sql_chain = (
            RunnablePassthrough.assign(schema=get_schema)
            | prompt
            | llm
            | StrOutputParser()
        )
        user_question = request.GET.get('user_question', '')
        #user_question = 'give me the schema of all the tables?'
        sql_query_result = sql_chain.invoke({"question": user_question})
        # sql_query_result = """ SELECT table_name, column_name, data_type
        # FROM information_schema.columns
        # WHERE table_schema = 'public'
        # ORDER BY table_name;
        # """
        # sql_query_result = """
        # SELECT * from blah limit 10;
        # """
        print("question: ",user_question.strip())
        print("SQL: ",sql_query_result)
        
        sql_output = "Something went wrong , check your question again"
        try:
            sql_output = db.run(sql_query_result)
            print("SQL output",sql_output)
            return JsonResponse({'message': sql_output})
        except ProgrammingError as e:
            
            print("An error occurred:\n", e)
            return JsonResponse({'message': f"Something went wrong with following error: \n{ e}: \n, check your question again"})

        finally:
            pass


 




    
