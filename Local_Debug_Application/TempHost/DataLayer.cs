using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TempHost
{
    static class DataLayer
    {
        public static double getAmbientTemp()
        {
            //Test vals
            Random rand = new Random();
            double currTemp = Math.Round(rand.NextDouble()*60, 1);

            //Data Call

            return currTemp;
        }

        public static double getAmbientHumidity()
        {
            //Test Vals
            Random rand = new Random();
            double currHumid = Math.Round(rand.NextDouble(), 2);

            //Data Call

            return currHumid;
        }

        public static bool getDatabaseStatus()
        {
            Random rand = new Random();
            bool status = rand.Next(0, 1) != 0;
            return status;
        }

        public static bool getPythonScriptStatus()
        {
            Random rand = new Random();
            bool status = rand.Next(0, 1) != 0;
            return status;
        }

        public static IEnumerable<DAO.TempLogEntry> GetTempHistory()
        {
            var tempData = new List<DAO.TempLogEntry>();
            tempData.Add(new DAO.TempLogEntry() { temp = 45.0, date = DateTime.Now });
            tempData.Add(new DAO.TempLogEntry() { temp = 44.3, date = DateTime.Now });
            tempData.Add(new DAO.TempLogEntry() { temp = 41.6, date = DateTime.Now });
            return tempData;
        }
    }
}
