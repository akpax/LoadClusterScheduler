import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

class ClusterVisualizer:
    def __init__(self):
        self.data = None
        self.labels = None
        self.dimension = None
        self.column_names = None
        self.centers = None
        self.output_dir = None

    def set_data(self, data, labels, centers=None):
        if isinstance(data, pd.DataFrame):
            # Store column names
            self.column_names = data.columns.tolist()
            # Convert DataFrame to numpy array
            data = data.values
        # Handling 1D data
        if data.ndim == 1 or (data.ndim == 2 and data.shape[1] == 1):
            self.data = data
            self.dimension = 1
        elif data.ndim == 2:
            self.dimension = data.shape[1]
            if self.dimension > 3:
                raise ValueError("Data with more than 3 dimensions is not supported")
            self.data = data
        else:
            raise ValueError("Unsupported data format")
        
        self.labels=labels
        if centers.any():
            self.centers=centers

    def plot(self, output_dir=None):
        if output_dir is not None:
            self.output_dir = output_dir
        if self.dimension == 1:
            self._plot_1d()
        elif self.dimension == 2:
            self._plot_2d()
        elif self.dimension == 3:
            self._plot_3d()
        else:
            raise ValueError("Data dimensionality not supported")

    def _plot_1d(self):
        # plt.scatter(self.data[:, 0], [0] * len(self.data), c=self.labels)
        for label in np.unique(self.labels):
            cluster_data = self.data[self.labels == label]
            plt.scatter(cluster_data, np.zeros(len(cluster_data)),  label=f'Cluster {label}')
        if self.centers is not None:
            plt.scatter(self.centers, [0] * len(self.centers), c='red', marker='x', label='Cluster Centers')
            plt.legend()
        plt.title("1D Cluster Visualization")
        plt.xlabel(self.column_names[0]) 
        if self.output_dir is not None:
            output_path = os.path.join(self.output_dir,"1D Cluster Visualization.png" )
            print(f"{output_path}=")
            plt.savefig(output_path, format="png")
        plt.show()

    def _plot_2d(self):
        # plt.ioff()  # Turn interactive mode off
        # Create a scatter plot for each cluster
        for label in np.unique(self.labels):
            cluster_data = self.data[self.labels == label]
            plt.scatter(cluster_data[:, 0], cluster_data[:, 1], label=f'Cluster {label}')
        # plt.scatter(self.data[:, 0], self.data[:, 1], c=self.labels)
        if self.centers is not None:
            plt.scatter(self.centers[:, 0], self.centers[:, 1], c='red', marker='x', label='Cluster Centers')
            plt.legend()
        plt.title("2D Cluster Visualization")
        plt.xlabel(self.column_names[0])
        plt.ylabel(self.column_names[1])
       #if self.output_dir is not None:
        output_path = os.path.join(self.output_dir,"2D Cluster Visualization.png" )
        print(f"{output_path}=")
        plt.savefig(output_path)
        plt.ion()
        plt.show()

    def _plot_3d(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        cmap = plt.get_cmap('viridis')  # Get a colormap
        unique_labels = np.unique(self.labels)
        colors = cmap(np.linspace(0, 1, len(unique_labels)))  # Generate colors

        for i, label in enumerate(unique_labels):
            cluster_data = self.data[self.labels == label]
            ax.scatter(cluster_data[:, 0], cluster_data[:, 1], cluster_data[:,2], label=f'Cluster {label}', color=colors[i])

        if self.centers is not None:
            ax.scatter(self.centers[:, 0], self.centers[:, 1], self.centers[:, 2], c='red', marker='x', label='Cluster Centers')

        ax.legend()
        ax.set_title("3D Cluster Visualization")
        ax.set_xlabel(self.column_names[0])
        ax.set_ylabel(self.column_names[1])
        ax.set_zlabel(self.column_names[2])
        if self.output_dir is not None:
            output_path = os.path.join(self.output_dir,"3D Cluster Visualization.png" )
            fig.savefig(output_path)
        plt.show()
        

        
