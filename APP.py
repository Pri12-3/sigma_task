{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPfihVVEGj0WrkgTp0FaWQ6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Pri12-3/sigma_task/blob/main/APP.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit pyngrok --quiet"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "X7n2I2vC-SGa",
        "outputId": "b3d0e3b2-6cab-43ff-f178-46ed50ce408d"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m1.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.9/9.9 MB\u001b[0m \u001b[31m53.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m80.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m5.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "from scipy.cluster.hierarchy import linkage, dendrogram, fcluster\n",
        "from sklearn.decomposition import PCA\n",
        "\n",
        "# Title\n",
        "st.title(\"Customer Segmentation using Hierarchical Clustering\")\n",
        "\n",
        "# File uploader\n",
        "uploaded_file = st.file_uploader(\"Upload your dataset (CSV)\", type=[\"csv\"])\n",
        "if uploaded_file is not None:\n",
        "    df = pd.read_csv(uploaded_file)\n",
        "\n",
        "    st.subheader(\"Raw Dataset\")\n",
        "    st.write(\"Dataset shape:\", df.shape)\n",
        "    st.dataframe(df.head())\n",
        "\n",
        "    st.title(\"Customer Segmentation with Hierarchical Clustering and PCA\")\n",
        "\n",
        "    # Drop irrelevant columns\n",
        "    drop_cols = ['ID', 'Dt_Customer', 'AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3',\n",
        "                 'AcceptedCmp4', 'AcceptedCmp5', 'Response']\n",
        "    df = df.drop(columns=drop_cols, errors='ignore')\n",
        "\n",
        "    # Create Age from Year_Birth\n",
        "    if 'Year_Birth' in df.columns:\n",
        "        df['Age'] = 2025 - df['Year_Birth']\n",
        "        df = df.drop(columns=['Year_Birth'])\n",
        "\n",
        "    # Fill missing numeric values with median\n",
        "    df = df.fillna(df.median(numeric_only=True))\n",
        "\n",
        "    # One-hot encode categorical variables\n",
        "    if 'Education' in df.columns and 'Marital_Status' in df.columns:\n",
        "        df = pd.get_dummies(df, columns=['Education', 'Marital_Status'], drop_first=True)\n",
        "\n",
        "    # Create Total Spending column\n",
        "    spending_cols = [c for c in df.columns if c.startswith('Mnt')]\n",
        "    df['Total_Spending'] = df[spending_cols].sum(axis=1)\n",
        "\n",
        "    # Select features\n",
        "    features = ['Age', 'Income', 'Kidhome', 'Teenhome', 'Recency', 'Complain',\n",
        "                'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases',\n",
        "                'NumStorePurchases', 'NumWebVisitsMonth', 'Total_Spending'] + \\\n",
        "               [c for c in df.columns if c.startswith('Education_') or c.startswith('Marital_Status_')]\n",
        "\n",
        "    df_features = df[features]\n",
        "\n",
        "    # Scale features\n",
        "    scaler = StandardScaler()\n",
        "    scaled_features = scaler.fit_transform(df_features)\n",
        "\n",
        "    st.write(\"### Features after scaling\")\n",
        "    st.dataframe(pd.DataFrame(scaled_features, columns=features).head())\n",
        "\n",
        "    # PCA\n",
        "    pca = PCA(n_components=2, random_state=42)\n",
        "    pca_features = pca.fit_transform(scaled_features)\n",
        "\n",
        "    st.write(f\"Explained variance by PCA components: {pca.explained_variance_ratio_}\")\n",
        "\n",
        "    # PCA scatter plot\n",
        "    plt.figure(figsize=(8, 6))\n",
        "    sns.scatterplot(x=pca_features[:, 0], y=pca_features[:, 1])\n",
        "    plt.title('PCA Scatter Plot (2 Components)')\n",
        "    st.pyplot(plt.gcf())\n",
        "    plt.clf()\n",
        "    plt.close()\n",
        "\n",
        "    # Hierarchical clustering\n",
        "    linked = linkage(scaled_features, method='ward')\n",
        "\n",
        "    # Dendrogram\n",
        "    plt.figure(figsize=(10, 5))\n",
        "    dendrogram(linked, truncate_mode='level', p=5)\n",
        "    plt.title('Hierarchical Clustering Dendrogram (truncated)')\n",
        "    plt.xlabel('Sample index or cluster size')\n",
        "    plt.ylabel('Distance')\n",
        "    st.pyplot(plt.gcf())\n",
        "    plt.clf()\n",
        "    plt.close()\n",
        "\n",
        "    # Slider for number of clusters\n",
        "    n_clusters = st.slider(\"Select number of clusters\", 2, 10, 4)\n",
        "\n",
        "    # Assign cluster labels\n",
        "    cluster_labels = fcluster(linked, t=n_clusters, criterion='maxclust')\n",
        "    df['Cluster'] = cluster_labels\n",
        "\n",
        "    st.write(\"### Cluster counts\")\n",
        "    st.write(df['Cluster'].value_counts().sort_index())\n",
        "\n",
        "    st.write(\"### Cluster summary (mean values)\")\n",
        "    st.write(df.groupby('Cluster')[features].mean().round(2))\n",
        "\n",
        "    # PCA scatter with cluster color\n",
        "    plt.figure(figsize=(8, 6))\n",
        "    sns.scatterplot(x=pca_features[:, 0], y=pca_features[:, 1], hue=cluster_labels, palette='Set2', s=50)\n",
        "    plt.title('PCA Scatter Plot colored by Cluster')\n",
        "    st.pyplot(plt.gcf())\n",
        "    plt.clf()\n",
        "    plt.close()\n",
        "\n",
        "else:\n",
        "    st.warning(\"Please upload a CSV file to proceed.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "3ptW1KTEGXoA",
        "outputId": "122244fd-414c-4d03-edd3-93656e06442d"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-05-21 13:45:58.216 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-21 13:45:58.731 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.11/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2025-05-21 13:45:58.742 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-21 13:45:58.754 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-21 13:45:58.759 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-21 13:45:58.760 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-21 13:45:58.761 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-21 13:45:58.762 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-21 13:45:58.770 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-21 13:45:58.777 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    }
  ]
}