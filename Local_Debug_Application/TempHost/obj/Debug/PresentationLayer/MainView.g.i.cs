﻿#pragma checksum "..\..\..\PresentationLayer\MainView.xaml" "{8829d00f-11b8-4213-878b-770e8597ac16}" "655CB0861114314B57AE66D7061669BFF8A2EBED5060F9BCE5DEB4F7E07EF9F0"
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version:4.0.30319.42000
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System;
using System.Diagnostics;
using System.Windows;
using System.Windows.Automation;
using System.Windows.Controls;
using System.Windows.Controls.Primitives;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Ink;
using System.Windows.Input;
using System.Windows.Markup;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Media.Effects;
using System.Windows.Media.Imaging;
using System.Windows.Media.Media3D;
using System.Windows.Media.TextFormatting;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Shell;
using TempHost;


namespace TempHost {
    
    
    /// <summary>
    /// MainWindow
    /// </summary>
    public partial class MainWindow : System.Windows.Window, System.Windows.Markup.IComponentConnector {
        
        
        #line 9 "..\..\..\PresentationLayer\MainView.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Grid baseGrid;
        
        #line default
        #line hidden
        
        
        #line 19 "..\..\..\PresentationLayer\MainView.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Grid HeaterToggleGrid;
        
        #line default
        #line hidden
        
        
        #line 26 "..\..\..\PresentationLayer\MainView.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Primitives.ToggleButton btnHeaterToggle;
        
        #line default
        #line hidden
        
        
        #line 29 "..\..\..\PresentationLayer\MainView.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Grid ReportGrid;
        
        #line default
        #line hidden
        
        
        #line 43 "..\..\..\PresentationLayer\MainView.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.TextBox txtDBStatus;
        
        #line default
        #line hidden
        
        
        #line 44 "..\..\..\PresentationLayer\MainView.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.TextBox txtAmbTemp;
        
        #line default
        #line hidden
        
        
        #line 45 "..\..\..\PresentationLayer\MainView.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Primitives.ToggleButton btnDBToggle;
        
        #line default
        #line hidden
        
        
        #line 49 "..\..\..\PresentationLayer\MainView.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Grid OptionsGrid;
        
        #line default
        #line hidden
        
        
        #line 56 "..\..\..\PresentationLayer\MainView.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Button btnAdvanced;
        
        #line default
        #line hidden
        
        
        #line 57 "..\..\..\PresentationLayer\MainView.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Button btnExit;
        
        #line default
        #line hidden
        
        
        #line 58 "..\..\..\PresentationLayer\MainView.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Button btnRefresh;
        
        #line default
        #line hidden
        
        private bool _contentLoaded;
        
        /// <summary>
        /// InitializeComponent
        /// </summary>
        [System.Diagnostics.DebuggerNonUserCodeAttribute()]
        [System.CodeDom.Compiler.GeneratedCodeAttribute("PresentationBuildTasks", "4.0.0.0")]
        public void InitializeComponent() {
            if (_contentLoaded) {
                return;
            }
            _contentLoaded = true;
            System.Uri resourceLocater = new System.Uri("/TempHost;component/presentationlayer/mainview.xaml", System.UriKind.Relative);
            
            #line 1 "..\..\..\PresentationLayer\MainView.xaml"
            System.Windows.Application.LoadComponent(this, resourceLocater);
            
            #line default
            #line hidden
        }
        
        [System.Diagnostics.DebuggerNonUserCodeAttribute()]
        [System.CodeDom.Compiler.GeneratedCodeAttribute("PresentationBuildTasks", "4.0.0.0")]
        [System.ComponentModel.EditorBrowsableAttribute(System.ComponentModel.EditorBrowsableState.Never)]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Design", "CA1033:InterfaceMethodsShouldBeCallableByChildTypes")]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Maintainability", "CA1502:AvoidExcessiveComplexity")]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1800:DoNotCastUnnecessarily")]
        void System.Windows.Markup.IComponentConnector.Connect(int connectionId, object target) {
            switch (connectionId)
            {
            case 1:
            this.baseGrid = ((System.Windows.Controls.Grid)(target));
            return;
            case 2:
            this.HeaterToggleGrid = ((System.Windows.Controls.Grid)(target));
            return;
            case 3:
            this.btnHeaterToggle = ((System.Windows.Controls.Primitives.ToggleButton)(target));
            
            #line 26 "..\..\..\PresentationLayer\MainView.xaml"
            this.btnHeaterToggle.Click += new System.Windows.RoutedEventHandler(this.btnHeaterToggle_Click);
            
            #line default
            #line hidden
            return;
            case 4:
            this.ReportGrid = ((System.Windows.Controls.Grid)(target));
            return;
            case 5:
            this.txtDBStatus = ((System.Windows.Controls.TextBox)(target));
            return;
            case 6:
            this.txtAmbTemp = ((System.Windows.Controls.TextBox)(target));
            return;
            case 7:
            this.btnDBToggle = ((System.Windows.Controls.Primitives.ToggleButton)(target));
            
            #line 45 "..\..\..\PresentationLayer\MainView.xaml"
            this.btnDBToggle.Click += new System.Windows.RoutedEventHandler(this.btnDBToggle_Click);
            
            #line default
            #line hidden
            return;
            case 8:
            this.OptionsGrid = ((System.Windows.Controls.Grid)(target));
            return;
            case 9:
            this.btnAdvanced = ((System.Windows.Controls.Button)(target));
            
            #line 56 "..\..\..\PresentationLayer\MainView.xaml"
            this.btnAdvanced.Click += new System.Windows.RoutedEventHandler(this.btnAdvanced_Click);
            
            #line default
            #line hidden
            return;
            case 10:
            this.btnExit = ((System.Windows.Controls.Button)(target));
            
            #line 57 "..\..\..\PresentationLayer\MainView.xaml"
            this.btnExit.Click += new System.Windows.RoutedEventHandler(this.btnExit_Click);
            
            #line default
            #line hidden
            return;
            case 11:
            this.btnRefresh = ((System.Windows.Controls.Button)(target));
            
            #line 58 "..\..\..\PresentationLayer\MainView.xaml"
            this.btnRefresh.Click += new System.Windows.RoutedEventHandler(this.btnRefresh_Click);
            
            #line default
            #line hidden
            return;
            }
            this._contentLoaded = true;
        }
    }
}

