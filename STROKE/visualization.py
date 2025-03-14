class visualization:
     def visualize_A_Column(self, column_name):
        """This function is used to visualize a column if a 
        column is numerical a histogram and a boxplot are 
        outputed otherwise a countplot is outputed
        """
        if column_name in self.data.columns:
            if self.data[column_name].dtype in ['float64' ,'int64']:
                fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 8))
                fig.patch.set_facecolor('lightblue')
                ax1.hist(x=self.data[column_name])
                ax1.set_title(column_name)
                ax1.set_xlabel(column_name)
                ax1.set_ylabel('Frequency')
                ax1.grid(True)
                ax1.set_facecolor('lightgray')

                ax2.boxplot(x=self.data[column_name])
                ax2.set_title(column_name)
                ax2.set_xlabel(column_name)
                ax2.set_ylabel("Frequency")
                ax2.grid(True)
                ax2.set_facecolor('lightgray')            
                
            else:
                sns.countplot(data=self.data, x=column_name)
                plt.title(column_name)
                plt.xlabel(column_name)
                plt.ylabel("Frequency")
                plt.grid()
    
            plt.show()
        else:
            print("Column not found")

    def visualization_numerical_columns(self):
        """This functions creates a figure and subplots where first
        axis is a histogram and second axis has a boxplot.
        """
        for i in self.data.columns:
          if self.data[i].dtype in ['float64' ,'int64'] and i != 'id':
            fig,(ax1,ax2)=plt.subplots(nrows=1,ncols=2,figsize=(10,8))
            fig.patch.set_facecolor('lightblue')

            ax1.hist(x=data[i])
            ax1.set_title(i)
            ax1.set_xlabel(i)
            ax1.set_ylabel('Frequency')  #   ax[0:0],ax[1:1]
            ax1.grid(True)
            ax1.set_facecolor('lightgray')

            ax2.boxplot(x=data[i])
            ax2.set_title(i)
            ax2.set_xlabel(i)
            ax2.set_ylabel("Frequency")
            ax2.grid(True)
            ax2.set_facecolor('lightgray')
        plt.show()    
    def visualization_categorical(self):
        """This functions creates a figure and subplots where first
        axis is a histogram and second axis has a boxplot.
        """
        for i in self.data.columns:
          if self.data[i].dtype in ['category'] and i != 'stroke':
            fig=plt.figure(figsize=(10,8))
            fig.patch.set_facecolor('lightblue')

            sns.countplot(data=data,x=i)
            plt.title(i)
            plt.xlabel(i)
            plt.ylabel("Frequency")
            plt.grid()
            #plt.set_facecolor('lightgray')
        plt.show()  