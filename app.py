import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('D:\startup.dashboard\startup1_cleaned.csv')
df['date'] = pd.to_datetime(df['date'])

def load_overall_analysis():
        st.title('Overall Analysis')

        #total investment
        total = round(df['amount'].sum())
        
        # max investment infused in startup
        max_funding = df.groupby('startup')['amount'].max().sort_values(ascending = False).head(1).values[0]

        #avg ticket size
        avg_funding = df.groupby('startup')['amount'].sum().mean()

        #total funded startup
        num_startup = df['startup'].nunique()  
        col1,col2,col3,col4 = st.columns(4)
        with col1:
                st.metric('Total',str(total)+' Cr')

        with col2:
                st.metric('Max',str(max_funding)+'Cr')        

        with col3:
                st.metric('Avg',str(avg_funding)+' Cr')
        
        with col4:
                st.metric('Funded Startup',num_startup)

        st.header('MoM Graph')
        df['month'] = df['date'].dt.month
        selected_option = st.selectbox('Select Type',['Total','Count'])
        if selected_option == 'Total':
                temp_df = df.groupby(['year','month'])['amount'].sum().reset_index()
        else:
                temp_df = df.groupby(['year','month'])['amount'].count().reset_index()
        temp_df['x_axis'] = temp_df['month'].astype(str) + '-' + temp_df['year'].astype(str) 

        fig4 ,ax4 =plt.subplots()
        ax4.plot(temp_df['x_axis'],temp_df['amount'])

        st.pyplot(fig4)       

def load_investor_detail(investor):
        st.title(investor)
        # load recent 5 investment of investor
        last_5df = df[df['investor'].str.contains('IDG Ventures')].head()[['date','startup','vertical','city','round','amount']]
        st.subheader('Most Recent Investments')
        st.dataframe(last_5df)
        

        col1,col2 = st.columns(2) 
        with col1:
            # Biggest investment
            big_series = df[df['investor'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False)
            st.subheader('Biggest Investments')
        
            fig ,ax =plt.subplots()
            ax.bar(big_series.index,big_series.values)

            st.pyplot(fig)

        with col2:
              verticle_series = df[df['investor'].str.contains(investor)].groupby('vertical')['amount'].sum()

              st.subheader('Sector invest in')

              fig1 ,ax1 =plt.subplots()
              ax1.pie(verticle_series,labels=verticle_series.index,autopct ='%0.01f%%')

              st.pyplot(fig1)
        
        # startup in city
        city_series = df[df['investor'].str.contains(' IDG Ventures')].groupby('city')['amount'].sum()
        st.subheader('City')

        fig2 ,ax2 =plt.subplots()
        ax2.pie(city_series,labels=city_series.index,autopct ='%0.01f%%')

        st.pyplot(fig2)
        
        # year by year investment
        df['date'] = pd.to_datetime(df['date'])
        df['year'] = df['date'].dt.year
        year_series = df[df['investor'].str.contains(investor)].groupby('year')['amount'].sum()

        st.subheader('YOY Investment')

        fig3 ,ax3 =plt.subplots()
        ax3.plot(year_series.index,year_series.values)

        st.pyplot(fig3)


st.sidebar.title('StartUp Funding Analysis')

option = st.sidebar.selectbox('Select One',['Overall Analysis','StartUp','Investor'])

if option == 'Overall Analysis':
        
        load_overall_analysis()
elif option == 'StartUp':
        st.sidebar.selectbox('Select StartUp',sorted(df['startup'].unique().tolist()))
        btn1 = st.sidebar.button("startup detail")
        st.title('StartUp Analysis')
else:
        
        select_investor = st.sidebar.selectbox('Select Investor',sorted(set(df['investor'].str.split(',').sum())))
        st.title('Investor Analysis')
        btn2 = st.sidebar.button('Investor detail')
        if btn2:
                load_investor_detail(select_investor)
   
df.info()   