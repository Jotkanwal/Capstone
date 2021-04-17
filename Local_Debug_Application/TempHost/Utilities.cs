using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace TempHost
{
    static class Utilities
    {
        static string pythonExecutableFP = "[Python Executable filepath]";
        static string pythonHeaterScriptFP = "[Heater Script filepath]";
        //static string dbExecutableFP = "[DB Init filepath]";
        //static string dbInitCommand = "[dbInitCommand]";

        public static void activateHeater()
        {
            try
            {
                //Start Py Script Process
                

                ProcessStartInfo startSettings = new ProcessStartInfo(@pythonExecutableFP);
                startSettings.Arguments = pythonHeaterScriptFP;
                startSettings.UseShellExecute = true; //Separate Process Instance, no need to directly read output
                startSettings.WindowStyle = ProcessWindowStyle.Minimized;

                var heaterProc = new Process();
                heaterProc.Start();
            }
            catch
            {
                //Disabled for testing while not on Pi
                //throw new OperationCanceledException();
            }
        }
        public static void deactivateHeater()
        {
            foreach(var proc in Process.GetProcesses().Where(p => p.ProcessName == "[PYTHON SHELL PROCESS NAME]"))
            {
                proc.Kill();
            }
        }

        public static void activateDB()
        {
            //Init MySQL DB process
        }
        public static void deactivateDB()
        {
            //Close MySQL DB process
        }

    }
}
