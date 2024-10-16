import torch
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#print("iterations")
#iterations = torch.load(os.path.join('simulations','output',experiment,'iterations.pt'))
#print(iterations.shape)

#print("X")
#X = torch.load(os.path.join('simulations','output',experiment,'X.pt'))
#print(X.shape)

def plot_calibration_predictions(experiment='',exclude_count=0):
    Y = torch.load(os.path.join('simulations','output',experiment,'Y.pt'))
    print(Y.shape)

    print("Y_pred_mean")
    Y_pred_mean = torch.load(os.path.join('simulations','output',experiment,'Y_pred_mean.pt'))
    print(Y_pred_mean.shape)

    print("Y_pred_var")
    Y_pred_var = torch.load(os.path.join('simulations','output',experiment,'Y_pred_var.pt'))
    print(Y_pred_var.shape)

    # Convert tensors to NumPy arrays
    Y = Y.numpy().flatten()
    mean = Y_pred_mean.numpy().flatten()
    var = Y_pred_var.numpy().flatten()
    n_missing=len(mean)-len(Y)
    if n_missing>0:
        Y=np.append(Y,np.repeat(0.1,n_missing))
        
    if len(mean) > exclude_count:
        Y = Y[exclude_count:]
        mean = mean[exclude_count:]
        var = var[exclude_count:]
        # Calculate standard deviation
        std_dev = np.sqrt(var)
        # Define confidence interval (e.g., 95% confidence interval)
        confidence_interval = 1.96 * std_dev
        # Define x values (e.g., indices or other x-axis values)
        x = np.arange(len(mean))
        # Plot the mean predictions
        plt.figure(figsize=(10, 6))
        plt.plot(x, mean, label='Predicted Mean', color='blue')
        # Plot the confidence interval
        plt.fill_between(x, mean - confidence_interval, mean + confidence_interval, color='blue', alpha=0.2, label='95% Confidence Interval')
        plt.plot(x,Y,label='Observation',marker='o',color='blue',linestyle='')
        # Add labels and title
        plt.xlabel('Index')
        plt.ylabel('Predicted Value')
        plt.title('Predictions with Confidence Interval')
        plt.legend()
        # Show the plot
        plt.show()
        # Save the plot
        plt.savefig(os.path.join("simulations","output",experiment,'_'.join((experiment,'predictions.png'))), dpi=300)  # Save as PNG with high resolution
        plt.savefig(os.path.join("simulations","output",experiment,'_'.join((experiment,'predictions.pdf'))))  
    else:
        print("The tensor length is less than or equal to the number of values to exclude.")


def plot_calibration_lengthscales(experiment=''):
    length_scales = torch.load(os.path.join('simulations','output',experiment,'length_scales.pt'))
    length_scales = torch.transpose(length_scales,0,1)
    nparam=list(length_scales.shape)[0]
    rounds=list(length_scales.shape)[1]
    parameter_names = pd.read_csv(os.path.join('simulations','test_parameter_key.csv'))
    parameter_names = parameter_names['parameter_label'].tolist()
    # plotting
    num_plots = nparam
    cols = int(np.ceil(np.sqrt(num_plots)))  # Number of columns in the grid
    rows = int(np.ceil(num_plots / cols)) 
    fig, axes = plt.subplots(rows, cols, figsize=(15, 2 * rows), sharex=True, sharey=True)
    axes = axes.flatten()  # Flatten the 2D array of axes to make indexing easier
    # Plot each row of the tensor
    x_values = torch.arange(rounds).tolist()
    for i in range(num_plots):
        axes[i].plot(x_values, length_scales[i].numpy(), marker='', linestyle='-')
        axes[i].set_title(f'{parameter_names[i]}')
        axes[i].set_ylabel('Length Scale')
        axes[i].set_xlabel('Batch')
    # Hide any unused subplots
    for j in range(num_plots, len(axes)):
        axes[j].axis('off')
    # Adjust layout
    plt.tight_layout()
    # Show plot
    plt.show()
    # Save the plot as PNG and PDF
    fig.savefig(os.path.join("simulations","output",experiment,'_'.join((experiment,'lengthscales.png'))), dpi=300)  # Save as PNG with high resolution
    fig.savefig(os.path.join("simulations","output",experiment,'_'.join((experiment,'lengthscales.pdf'))))  


def plot_calibration_timing(experiment=''):
    timer_model = torch.load(os.path.join('simulations','output',experiment,'timer_model.pt'))
    timer_batch_generator = torch.load(os.path.join('simulations','output',experiment,'timer_batch_generator.pt'))
    timer_model = timer_model.numpy().flatten()
    timer_batch_generator = timer_batch_generator.numpy().flatten()
    # Define x values (e.g., indices or other x-axis values)
    x = np.arange(len(timer_model))
    # Plot the mean predictions
    plt.figure(figsize=(10, 6))
    plt.plot(x, timer_model, label='Model Fitting', color='blue')
    plt.plot(x, timer_batch_generator, label='Posterior Sampling', color='red')
    # Add labels and title
    plt.xlabel('Batch')
    plt.ylabel('Time (sec)')
    plt.title('Timing')
    plt.legend()
    # Show the plot
    plt.show()
    # Save plot
    plt.savefig(os.path.join("simulations","output",experiment,'_'.join((experiment,'timing.png'))), dpi=300)  # Save as PNG with high resolution
    plt.savefig(os.path.join("simulations","output",experiment,'_'.join((experiment,'timing.pdf'))))
