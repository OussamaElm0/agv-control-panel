# Import necessary libraries
import os
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from commandes.models import Commande

def commands_last_week():
    # Calculate the start and end dates for the last week
    end_date = timezone.now()
    start_date = end_date - timedelta(days=7)

    # Filter Commande objects for the last week
    commandes_last_week = Commande.objects.filter(date__gte=start_date, date__lte=end_date)

    # Group Commande objects by date and count the number of Commandes for each date
    commands_per_day_last_week = commandes_last_week.values('date').annotate(total_commandes=Count('id'))

    # Extract dates and corresponding command counts
    dates = [entry['date'] for entry in commands_per_day_last_week]
    command_counts = [entry['total_commandes'] for entry in commands_per_day_last_week]

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(dates, command_counts, marker='o', linestyle='-')
    plt.xlabel('Date')
    plt.ylabel('Number of Commands')
    plt.title('Commands per Day in Last Week')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()

    # Display the plot
    plt.show()

# Call the function to generate and display the plot
commands_last_week()
