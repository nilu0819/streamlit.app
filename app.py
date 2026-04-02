import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

# Title
st.title("K-Means Clustering on Mall Customers Dataset")

# Upload dataset
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    dataset = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview")
    st.write(dataset.head())

    # Select features
    st.write("### Feature Selection")
    x_col = st.selectbox("Select X-axis feature", dataset.columns)
    y_col = st.selectbox("Select Y-axis feature", dataset.columns)
    X = dataset[[x_col, y_col]].values

    # Elbow Method
    st.write("### Elbow Method")
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init="k-means++", random_state=0)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    fig, ax = plt.subplots()
    ax.plot(range(1, 11), wcss, marker="o")
    ax.set_title("The Elbow Method")
    ax.set_xlabel("Number of clusters")
    ax.set_ylabel("WCSS")
    st.pyplot(fig)

    # Choose number of clusters
    n_clusters = st.slider("Select number of clusters", 2, 10, 5)

    # Train KMeans
    kmeans = KMeans(n_clusters=n_clusters, init="k-means++", random_state=0)
    y_kmeans = kmeans.fit_predict(X)

    # Visualize clusters
    st.write("### Clusters Visualization")
    fig, ax = plt.subplots()
    colors = ["red", "blue", "green", "cyan", "magenta", "orange", "purple", "brown", "pink", "gray"]

    for i in range(n_clusters):
        ax.scatter(X[y_kmeans == i, 0], X[y_kmeans == i, 1], s=100, c=colors[i], label=f"Cluster {i+1}")

    ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c="yellow", label="Centroids")
    ax.set_title("Clusters of Customers")
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.legend()
    st.pyplot(fig)

    # Add cluster column to dataset
    dataset["Cluster"] = y_kmeans
    st.write("### Dataset with Cluster Labels")
    st.write(dataset.head())
