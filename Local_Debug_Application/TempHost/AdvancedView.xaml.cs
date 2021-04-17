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
using System.Windows.Shapes;

namespace TempHost
{
    /// <summary>
    /// Interaction logic for AdvancedView.xaml
    /// </summary>
    public partial class AdvancedView : Window
    {
        public string AmbientTemp { get { return _ambientTemp.ToString(); } }
        private double _ambientTemp { get { return DataLayer.getAmbientTemp(); } }
        public string AmbientHumid { get { return _ambientHumid.ToString(); } }
        private double _ambientHumid { get { return DataLayer.getAmbientHumidity(); } }


        public AdvancedView()
        {
            InitializeComponent();
            WindowStartupLocation = System.Windows.WindowStartupLocation.CenterScreen;
            refreshPage();
        }

        private void btnBack_Click(object sender, RoutedEventArgs e)
        {
            MainWindow mainView = new MainWindow();
            mainView.Show();
            this.Close();
        }
        private void refreshPage()
        {
            txtCurrTemp.Text = AmbientTemp;
            txtCurrHumidity.Text = AmbientHumid;
        }

        private void btnTempLog_Click(object sender, RoutedEventArgs e)
        {
            var tempView = new TempHistoryView();
            tempView.ShowDialog();
        }

        private void btnTempSched_Click(object sender, RoutedEventArgs e)
        {
            var tempSchedView = new TempScheduleView();
            tempSchedView.ShowDialog();
        }
    }
}
