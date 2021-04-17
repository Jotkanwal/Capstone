using System;
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
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Timers;

namespace TempHost
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public string AmbientTemp { get { return _ambientTemp.ToString(); } }
        private double _ambientTemp { get { return DataLayer.getAmbientTemp(); } }

        public MainWindow()
        {
            InitializeComponent();
            WindowStartupLocation = System.Windows.WindowStartupLocation.CenterScreen;
            pageRefresh();
        }

        private void btnAdvanced_Click(object sender, RoutedEventArgs e)
        {
            AdvancedView advView = new AdvancedView();
            advView.Show();
            this.Close();
        }

        private void btnExit_Click(object sender, RoutedEventArgs e)
        {
            System.Environment.Exit(1);
        }

        private void btnHeaterToggle_Click(object sender, RoutedEventArgs e)
        {
            if (btnHeaterToggle.Content.ToString() == "ON")
            {
                try { Utilities.deactivateHeater(); }
                catch (Exception)
                {
                    MessageBoxResult result = MessageBox.Show("The Heater failed to shut down correctly. Reattempt?", "Shutdown Failed", MessageBoxButton.YesNo, MessageBoxImage.Question);
                    if (result == MessageBoxResult.Yes) { btnHeaterToggle_Click(sender, e); }
                    return;
                }
                btnHeaterToggle.Content = "OFF";
            }
            else
            {
                try { Utilities.activateHeater(); }
                catch (Exception)
                {
                    MessageBoxResult result = MessageBox.Show("The Heater failed to initialize. Reattempt?", "Startup Failed", MessageBoxButton.YesNo, MessageBoxImage.Question);
                    if (result == MessageBoxResult.Yes) { btnHeaterToggle_Click(sender, e); }
                    return;
                }
                btnHeaterToggle.Content = "ON";
            }
        }

        private void btnDBToggle_Click(object sender, RoutedEventArgs e)
        {
            if (btnDBToggle.Content.ToString() == "ON")
            {
                try { Utilities.deactivateDB(); }
                catch (Exception)
                {
                    MessageBoxResult result = MessageBox.Show("The Database failed to shut down correctly. Reattempt?", "Shutdown Failed", MessageBoxButton.YesNo, MessageBoxImage.Question);
                    if (result == MessageBoxResult.Yes) { btnDBToggle_Click(sender, e); }
                    return;
                }
                btnDBToggle.Content = "OFF";
            }
            else
            {
                try { Utilities.activateDB(); }
                catch (Exception)
                {
                    MessageBoxResult result = MessageBox.Show("The Database failed to initialize. Reattempt?", "Startup Failed", MessageBoxButton.YesNo, MessageBoxImage.Question);
                    if (result == MessageBoxResult.Yes) { btnDBToggle_Click(sender, e); }
                    return;
                }
                btnDBToggle.Content = "ON";
            }
        }

        private void pageRefresh()
        {
            txtAmbTemp.Text = AmbientTemp;
        }

        private void btnRefresh_Click(object sender, RoutedEventArgs e)
        {
            pageRefresh();
        }
    }
}
