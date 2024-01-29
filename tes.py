import streamlit as st
import pandas as pd


st.set_page_config(page_title='R cheat sheet', layout='wide',
                
)

st.sidebar.title("R cheat sheet")
st.sidebar.caption("made by asahcvulas")

with st.sidebar.expander("GETTING HELP"):
    st.subheader("Accesing the help files")
    st.code("?mean")
    st.caption("Get help of a particular function")
    st.code("help.search(‘weighted mean’)")
    st.caption("Search for help on a particular topic")
    st.code("help(package = ‘dplyr’)")
    st.caption("Get help on a particular package")

    st.subheader("More About an Object")
    st.code("str(iris)")
    st.caption("Get a summary of an object’s structure. ")
    st.code("class(iris)")
    st.caption("Find the class an object belongs to.")

with st.sidebar.expander("USING LIBRARIES"):
    st.code("install.packages(‘dplyr’)")
    st.caption("Download and install a package from CRAN")
    st.code("library(dplyr)")
    st.caption("Load the package into the session, making all its functions available to use.")
    st.code("dplyr::select")
    st.caption("Use a particular function from a package.")
    st.code("data(iris)")
    st.caption("Load a built-in dataset into the environment. ")

with st.sidebar.expander("WORKING DIRECTORY"):
    st.code("getwd()")
    st.caption("Get the current working directory")
    st.code("setwd(‘/Users/username/Documents’)")
    st.caption("Set the current working directory")
    st.markdown("`Use projects in RStudio to set the working directory to the folder you are working in.`")

st.title("R cheat sheet")
cols =  st.columns(2)

def st_code_block(caption=None, code=None):
    st.caption(f"{caption}")
    st.code(code, language="r")


def vectors():
    st.header("Vectors")
    creating_vectors, vectors_functions, selecting_vector_elements = \
    st.tabs(["Creating Vectors", "Vectors Functions", "Selecting Vector Elements"])

    with creating_vectors:
        data = {
            'syntax' : ['c(2, 4, 6)', '2:6', 'seq(2, 3, by=0.5)',  'rep(1:2, times=3)', 'rep(1:2, each=3)'],
            'output' : ['2 4 6', '2 3 4 5 6', '2.0 2.5 3.0 3.5', '1 2 1 2 1 2', '1 1 1 2 2 2']
        }
        df = pd.DataFrame(data)
        st.table(df)

    with vectors_functions:
        st_code_block("Return x sorted.", "sort(x)")
        st_code_block("Return x reversed.", "rev(x)")
        st_code_block("See counts of values.", "table(x)")
        st_code_block("Return unique values.", "unique(x)")
    
    with selecting_vector_elements:
        st.subheader("by position")
        position = {
            'syntax' : ['x[1]', 'x[-4]', 'x[2:4]', 'x[-(2:4)] ', 'x[c(1, 5)]'],
            'Description' : ['The fourth element.', 'All but the fourth.', 'Elements two to four', 'All elements except two to four', 'Elements one and five.']
        }

        df_position = pd.DataFrame(position)
        st.table(df_position)

        st.subheader("by value")
        value = {
            'syntax' : ['x[x == 10]', 'x[x < 0]', 'x[x %in% c(1, 2, 5)]'],
            'Description' : ['Elements which are equal to 10', 'All elements less than zero.', 'Elements in the set 1, 2, 5.']
        }

        df_value = pd.DataFrame(value)
        st.table(df_value)


def programming():
    st.subheader("Programming")
    for_loop, while_loop, if_statement, functions, condition = \
    st.tabs(["For Loop", "While Loop", "If Statement", "Functions", "Condition"])

    with for_loop:
        st_code_block("For loop", 
                      """
                for (variable in sequence){
                    Do something 
                }
                  """)
        st_code_block("example",
                      """
                    for (i in 1:4){
                        j <- i + 10 
                        print(j) 
                    }
                     """)
    with while_loop:
        st_code_block("While loop", 
                      """
                    while (condition){
                        Do something 
                    }
                  """)
        st_code_block("example",
                      """
                    while (i < 5){
                        print(i) 
                        i <- i + 1 
                    }
                     """)
    with if_statement:
        st_code_block("If statement", 
                      """
                    if (condition){
                        Do something 
                    }
                  """)
        st_code_block("example",
                      """
                    if (x > 0){
                        print("x is positive") 
                    }
                     """)
    with functions:
        st_code_block("Functions", 
                      """
                    function_name <- function(arg1, arg2){
                        Do something 
                        return(something) 
                    }
                  """)
        st_code_block("example",
                      """
                    sum <- function(x, y){
                        result <- x + y 
                        return(result) 
                    }
                     """)
    with condition:
        condition = {
            'syntax' : ['a == b', 'a != b', 'a > b', 'a < b', 'a >= b', 'a <= b', 'is.na(a)', 'is.null(a)'],
            'Description' : ['a equals b', 'a does not equal b', 'a is greater than b', 'a is less than b', 'a is greater than or equal to b', 'a is less than or equal to b', 'a is NA', 'a is NULL']
        }

        df_condition = pd.DataFrame(condition)
        st.table(df_condition)


def r_w_data():
    st.header("Reading and Writing Data")
    r_w = {
        'reading' : ['df <- read.table(‘file.txt’)', 'df <- read.csv(‘file.csv’)', 'load(‘file.RData’)'],
        'writing' : ['write.table(df, ‘file.txt’)', 'write.csv(df, ‘file.csv’)', 'save(df, file=‘file.RData’)'],
        'Description' : ['Read and Write a text file.', 'Read and Write a CSV file.', 'Read and Write a binary file.']
    }

    df_r_w = pd.DataFrame(r_w)
    st.table(df_r_w)

def operator():
    st.subheader("Operators")
    arithmatic, logical, assignment, other = \
    st.tabs(["Arithmatic", "Logical", "Assignment", "Other"])

    with arithmatic:
        st.subheader("Arithmatic")
        arithmatic = {
            'Operator' : ['x + y', 'x - y', 'x * y', 'x / y', 'x ^ y', 'x %% y', 'x %/% y'],
            'Description' : ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Exponentiation', 'Modulo', 'Integer division']
        }
        df_arithmatic = pd.DataFrame(arithmatic)
        st.table(df_arithmatic)
    
    with logical:
        st.subheader("logical")
        logical = {
            'Operator' : ['!', '&', '&&', '|', '||'],
            'Description' : ['Logical NOT', 'Element-wise Logical AND', 'Logical AND', 'Element-wise Logical OR', 'Logical OR']
        }
        df_logical = pd.DataFrame(logical)
        st.table(df_logical)
    with assignment:
        st.subheader("Assignment")
        st_code_block("Assigns a variable to x",
                      """
                      x <- 5
                      x = 5
                      """)
    with other:
        st.subheader("Other")
        other = {
            'Operator' : [' %in% ', '$', '%>%'],
            'Description' : ['Identifies whether an element belongs to a vector', 'Allows you to access objects stored within an object', 'Part of magrittr package, it’s used to pass objects to functions']
        }
        df_other = pd.DataFrame(other)
        st.table(df_other)

def math():
    st.subheader("Math Functions")
    math = {
        'Function' : ['abs(x)', 'sqrt(x)', 'ceiling(x)', 'floor(x)', 'round(x, digits=n)', 'trunc(x)', 'signif(x, digits=n)', 'log(x, base=b)', 'log10(x)', 'log2(x)', 'exp(x)', 'factorial(x)', 'choose(n, k)', 'gamma(x)', 'lgamma(x)', 'sin(x)', 'cos(x)', 'tan(x)', 'asin(x)', 'acos(x)', 'atan(x)', 'sinh(x)', 'cosh(x)', 'tanh(x)', 'asinh(x)', 'acosh(x)', 'atanh(x)'],
        'Description' : ['Absolute value', 'Square root', 'Rounds up', 'Rounds down', 'Rounds to n digits', 'Truncates', 'Rounds to n significant digits', 'Natural log', 'Log base 10', 'Log base 2', 'Exponential', 'Factorial', 'Combinations', 'Gamma function', 'Log of gamma function', 'Sine', 'Cosine', 'Tangent', 'Arcsine', 'Arccosine', 'Arctangent', 'Hyperbolic sine', 'Hyperbolic cosine', 'Hyperbolic tangent', 'Hyperbolic arcsine', 'Hyperbolic arccosine', 'Hyperbolic arctangent']
    }
    df_math = pd.DataFrame(math)
    st.table(df_math)



left_column_defaults = ['Vectors', 'Reading and Writing Data', 'Math Functions']
right_column_defaults = ['Programming', 'Operators']
all_segments = left_column_defaults + right_column_defaults

def default_layout():
    st.session_state["layout_left_column"] = left_column_defaults
    st.session_state["layout_right_column"] = right_column_defaults

custom_layout = st.sidebar.expander("🧑‍🎨 Customize Layout")

with custom_layout:
    st.button("Default Layout", on_click=default_layout)
    side_left_col, side_right_col = st.columns(2)
    left_col_segments = side_left_col.multiselect("Left Column", 
                          options=all_segments, 
                          default=left_column_defaults,
                          key="layout_left_column")
                          
    right_col_segments = side_right_col.multiselect("Right Column", 
                          options=all_segments, 
                          default=right_column_defaults,
                          key="layout_right_column")
segment_dict= {
    "Vectors": vectors,
    "Programming": programming,
    "Reading and Writing Data": r_w_data,
    "Operators": operator,
    "Math Functions": math
}

with cols[0]:
    for seg in left_col_segments:
        segment_dict[seg]()
    

with cols[1]:
    for seg in right_col_segments:
        segment_dict[seg]()



                    





    