   M S B A M L   `   `   `  ����C  ?TempHost, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null#clr-namespace:TempHostTempHost  5   	       TempHost.MainWindow   5   	   \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   (localclr-namespace:TempHost     5   	     � Title$  Cabinet Controller��5   	   $	��300��6$   $	��350��61   .��5	      � -   5        $��baseGrid��5	      $��10 10 10 10q�6    � RowDefinitions 5
   
   �� 5      $��20 �6   �� 5      $
��auto �6   �� 5      $
��auto �6   �� 5      $
��auto �6   �� 5      $
��auto �6   �� 5      $��20 �6   .+�5   
   � -   5        $��HeaterToggleGrid��5      $��1��6   $��0 0 0 20q�64    5      �� 5      $
��auto �6    �� 5      $
��auto �6    .+�5      �� $��Heater��6   $��0��6&   $��Center=�63   d� 5      -   5         d�Name$ btnHeaterToggle��5      $	��OFF��64   $��1��6B   $��20��6O   $��50��6[   $��	10 0 10 0q�6�   5      � 5   
   -   5        $��
ReportGrid��5      $��2��6    � ColumnDefinitions 5      �� 5      $
��auto �6#   �� 5       $
��auto �6#   .+�5"      �� $��0��6   .+�5#      �� $��Temperature Target:��6   $��0��6a    �� Target 66   ��  �� ElementName$ txtDbStatus��6a   �� 5%      $"��Current Ambient Temperature:��6   $��0��6i    6?   �� $ 
txtAmbTemp��6i   �� 5'      $��Database Status:��6   $��0��6^    63   �� $ btnDBToggle��6^   5)      �� 5*      $��1��6   .+�5+      �� -   5        $��txtDBStatus��5+      $��1��6-   $��50��6=   $��0 5 0 0q�6H   �� 5,      -   5        $��
txtAmbTemp��5,      $��1��6,   $��50��6<    �� 
IsReadOnly . $��0 7 0 0q�6Y   d� 5-      -   5        $ btnDBToggle��5-      $	��OFF��6N   $��0 10 0 0q�6\   5.      5/      � 51   
   -   5        $��OptionsGrid��51      $��3��6    52      �� 53      $
��auto �6#   �� 54      $
��auto �6#   �� 55      $
��auto �6#   .+�58      �� -	   5         ��Name$ btnAdvanced��58      $��Advanced Settings��6D   $��0��6`   $��10 10 10 10q�6p   $��	10 2 10 3q�6�   �� 59      -
   5        $ btnExit��59      $
��Exit��6=   $��1��6L   $��10 10 10 10q�6\   $��	10 2 10 3q�6q   �� 5:      -   5        $ 
btnRefresh��5:      $��Refresh Values��6B   $��2��6[   $��10 10 10 10q�6l   $��	10 2 10 3q�6�   5;      5=      5>      