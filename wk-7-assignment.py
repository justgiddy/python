# Data Analysis and Visualization Assignment
# Using the Iris Dataset for demonstration

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.datasets import load_iris
import warnings
warnings.filterwarnings('ignore')

# Set style for better looking plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("🌸 IRIS DATASET ANALYSIS AND VISUALIZATION")
print("=" * 50)

# Task 1: Load and Explore the Dataset
def load_and_explore_data():
    """Load the Iris dataset and perform initial exploration"""
    print("\n📊 TASK 1: LOADING AND EXPLORING THE DATASET")
    print("-" * 40)
    
    try:
        # Load Iris dataset from sklearn
        iris = load_iris()
        
        # Create DataFrame
        df = pd.DataFrame(iris.data, columns=iris.feature_names)
        df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
        
        print("✅ Dataset loaded successfully!")
        print(f"📁 Dataset shape: {df.shape}")
        
        # Display first few rows
        print("\n🔍 First 5 rows of the dataset:")
        print(df.head())
        
        # Explore dataset structure
        print("\n📋 Dataset information:")
        print(df.info())
        
        # Check for missing values
        print("\n🔎 Missing values check:")
        missing_data = df.isnull().sum()
        print(missing_data)
        
        # Since Iris dataset is clean, we'll demonstrate cleaning with a hypothetical scenario
        print("\n🧹 Data cleaning demonstration:")
        if df.isnull().sum().sum() == 0:
            print("✅ No missing values found. Dataset is already clean!")
        else:
            # This would execute if there were missing values
            df_cleaned = df.dropna()  # or df.fillna(method='ffill')
            print(f"Cleaned dataset shape: {df_cleaned.shape}")
        
        return df
    
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return None

# Task 2: Basic Data Analysis
def perform_data_analysis(df):
    """Perform basic statistical analysis on the dataset"""
    print("\n📈 TASK 2: BASIC DATA ANALYSIS")
    print("-" * 40)
    
    # Basic statistics
    print("📊 Basic statistics for numerical columns:")
    print(df.describe())
    
    # Statistics by species
    print("\n🌿 Statistics grouped by species:")
    numerical_cols = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    
    for col in numerical_cols:
        print(f"\n{col} by species:")
        species_stats = df.groupby('species')[col].agg(['mean', 'median', 'std', 'min', 'max'])
        print(species_stats)
    
    # Correlation analysis
    print("\n🔗 Correlation matrix for numerical features:")
    correlation_matrix = df[numerical_cols].corr()
    print(correlation_matrix)
    
    # Interesting findings
    print("\n💡 INTERESTING FINDINGS:")
    print("• Setosa species has significantly smaller petals than other species")
    print("• Virginica has the largest petals on average")
    print("• Sepal dimensions show less variation between species compared to petals")
    print("• Strong positive correlation between petal length and petal width")

# Task 3: Data Visualization
def create_visualizations(df):
    """Create various visualizations to understand the data"""
    print("\n🎨 TASK 3: DATA VISUALIZATION")
    print("-" * 40)
    
    # Create a figure with multiple subplots
    fig = plt.figure(figsize=(20, 15))
    
    # 1. Line Chart - Trends by species (using index as pseudo-time)
    print("📈 Creating Line Chart...")
    ax1 = plt.subplot(2, 3, 1)
    species_colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
    
    for species in df['species'].unique():
        species_data = df[df['species'] == species]
        plt.plot(species_data.index[:30], species_data['sepal length (cm)'][:30], 
                label=species, color=species_colors[species], marker='o', linewidth=2)
    
    plt.title('Sepal Length Trends (First 30 Samples)', fontsize=14, fontweight='bold')
    plt.xlabel('Sample Index')
    plt.ylabel('Sepal Length (cm)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 2. Bar Chart - Average measurements by species
    print("📊 Creating Bar Chart...")
    ax2 = plt.subplot(2, 3, 2)
    numerical_cols = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    
    # Calculate means
    species_means = df.groupby('species')[numerical_cols].mean()
    
    # Plot grouped bar chart
    x = np.arange(len(species_means.index))
    width = 0.2
    
    for i, col in enumerate(numerical_cols):
        plt.bar(x + i*width, species_means[col], width, label=col, alpha=0.8)
    
    plt.title('Average Measurements by Species', fontsize=14, fontweight='bold')
    plt.xlabel('Species')
    plt.ylabel('Measurement (cm)')
    plt.xticks(x + width*1.5, species_means.index)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3, axis='y')
    
    # 3. Histogram - Distribution of sepal length
    print("📊 Creating Histogram...")
    ax3 = plt.subplot(2, 3, 3)
    
    for species in df['species'].unique():
        species_data = df[df['species'] == species]
        plt.hist(species_data['sepal length (cm)'], alpha=0.7, label=species, 
                bins=15, edgecolor='black')
    
    plt.title('Distribution of Sepal Length by Species', fontsize=14, fontweight='bold')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 4. Scatter Plot - Sepal length vs Petal length
    print("🔵 Creating Scatter Plot...")
    ax4 = plt.subplot(2, 3, 4)
    
    for species in df['species'].unique():
        species_data = df[df['species'] == species]
        plt.scatter(species_data['sepal length (cm)'], species_data['petal length (cm)'],
                   label=species, alpha=0.7, s=60)
    
    plt.title('Sepal Length vs Petal Length', fontsize=14, fontweight='bold')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 5. Box Plot - Distribution comparison
    print("📦 Creating Box Plot...")
    ax5 = plt.subplot(2, 3, 5)
    
    df_melted = pd.melt(df, id_vars=['species'], value_vars=numerical_cols,
                       var_name='Measurement', value_name='Value')
    
    sns.boxplot(data=df_melted, x='Measurement', y='Value', hue='species')
    plt.title('Distribution of Measurements by Species', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # 6. Heatmap - Correlation matrix
    print("🔥 Creating Heatmap...")
    ax6 = plt.subplot(2, 3, 6)
    
    correlation_matrix = df[numerical_cols].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
                square=True, fmt='.2f', cbar_kws={'shrink': 0.8})
    plt.title('Feature Correlation Heatmap', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.show()
    
    print("✅ All visualizations created successfully!")

# Additional Analysis
def additional_insights(df):
    """Provide additional insights and observations"""
    print("\n🔍 ADDITIONAL INSIGHTS AND OBSERVATIONS")
    print("-" * 40)
    
    # Species distribution
    print("🌿 Species Distribution:")
    species_counts = df['species'].value_counts()
    print(species_counts)
    
    # Most distinctive feature
    print("\n🎯 Most Distinctive Feature Between Species:")
    numerical_cols = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    
    for col in numerical_cols:
        variance_ratio = df.groupby('species')[col].std().mean() / df[col].std()
        print(f"{col}: Variance ratio = {variance_ratio:.3f}")
    
    # Key observations
    print("\n📝 KEY OBSERVATIONS:")
    print("1. Setosa is clearly separable from other species based on petal measurements")
    print("2. Versicolor and Virginica show some overlap but are generally separable")
    print("3. Petal measurements are more useful for classification than sepal measurements")
    print("4. The dataset is well-balanced with 50 samples per species")
    print("5. Strong correlations exist between petal dimensions")

# Main execution
def main():
    """Main function to run the complete analysis"""
    try:
        # Task 1: Load and explore data
        df = load_and_explore_data()
        
        if df is not None:
            # Task 2: Perform data analysis
            perform_data_analysis(df)
            
            # Task 3: Create visualizations
            create_visualizations(df)
            
            # Additional insights
            additional_insights(df)
            
            print("\n🎉 ANALYSIS COMPLETED SUCCESSFULLY!")
            print("=" * 50)
            
            # Save the cleaned dataset
            df.to_csv('iris_cleaned_dataset.csv', index=False)
            print("💾 Cleaned dataset saved as 'iris_cleaned_dataset.csv'")
            
        else:
            print("❌ Failed to load dataset. Analysis cannot proceed.")
    
    except Exception as e:
        print(f"❌ An error occurred during analysis: {e}")
        import traceback
        traceback.print_exc()

# Run the analysis
if __name__ == "__main__":
    main()
