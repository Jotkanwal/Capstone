﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace TempHost
{
    /// <summary>
    /// Interaction logic for TempHistoryView.xaml
    /// </summary>
    public partial class TempHistoryView : Window
    {
        public TempHistoryView()
        {
            InitializeComponent();
            WindowStartupLocation = System.Windows.WindowStartupLocation.CenterScreen;
            loadTableData();
        }

        private void loadTableData()
        {
            tblTempHistory.DataContext = DataLayer.GetTempHistory();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {

        }

        private void btnBack_Click(object sender, RoutedEventArgs e)
        {
            this.Close();
        }
    }
}
