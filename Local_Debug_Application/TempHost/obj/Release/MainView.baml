   M S B A M L   `   `   `  ���� C  ?TempHost, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null#clr-namespace:TempHostTempHost      TempHost.MainWindow   \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     @d2http://schemas.microsoft.com/expression/blend/2008     Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     (localclr-namespace:TempHost       � Title$  Cabinet Controller��$	��300��$	��350��.��� -   $��baseGrid��$��10 10 10 10q� � RowDefinitions �� $��20 ��� $
��auto ��� $
��auto ��� $
��auto ��� $
��auto ��� $��20 �.+�� -   $��HeaterToggleGrid��$��1��$��0 0 0 20q� �� $
��auto ��� $
��auto �.+��� $��Heater��$��0��$��Center=�d� -    d�Name$ btnHeaterToggle��$	��OFF��$��1��$��20��$��50��$��	10 0 10 0q�� -   $��
ReportGrid��$��2�� � ColumnDefinitions �� $
��auto ��� $
��auto �.+��� $��0��.+��� $��Temperature Target:��$��0�� �� Target ��  �� ElementName$ txtDbStatus���� $"��Current Ambient Temperature:��$��0�� �� $ 
txtAmbTemp���� $��Database Status:��$��0�� �� $ btnDBToggle���� $��1��.+��� -   $��txtDBStatus��$��1��$��50��$��0 5 0 0q��� -   $��
txtAmbTemp��$��1��$��50�� �� 
IsReadOnly . $��0 7 0 0q�d� -   $ btnDBToggle��$	��OFF��$��0 10 0 0q�� -   $��OptionsGrid��$��3�� �� $
��auto ��� $
��auto ��� $
��auto �.+��� -	    ��Name$ btnAdvanced��$��Advanced Settings��$��0��$��10 10 10 10q�$��	10 0 10 2q��� -
   $ btnExit��$
��Exit��$��1��$��10 10 10 10q�$��	10 0 10 2q��� -   $ 
btnRefresh��$��Refresh Values��$��2��$��10 10 10 10q�$��	10 0 10 3q�