   M S B A M L   `   `   `  ����C  ?TempHost, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null#clr-namespace:TempHostTempHost  5   	       TempHost.TempHistoryView   5   	   \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   (localclr-namespace:TempHost     5   	     � Title$  TempHistoryView��5   	   $	��450��6!   $	��800��6.   .��5	      � $��10 10 10 10q�6    � RowDefinitions 5
   
   �� 5      $��20 �6   �� 5      $
��auto �6   �� 5      $
��auto �6   �� 5      $��* �6   �� 5      $
��auto �6   .+�5   
   �� $��1��6   Temperature Logging67   &   System.Windows.Controls.DataGrid  5   
   -   5          Name$ tblTempHistory��5       $��2��6      
IsReadOnly .    CanUserResizeRows .     AutoGenerateColumns .  $��10 10 10 10q�6�   ��68   ��    Columns 5      0  *System.Windows.Controls.DataGridTextColumn  5      ,  &System.Windows.Controls.DataGridColumn   Header$ Temperature��6%   1  +System.Windows.Controls.DataGridBoundColumn   Binding 6:   �� *temp+  5      $ Upload Time��6%   	   Width5  /System.Windows.Controls.DataGridLengthConverter$	 * 6S    6:   �� *date+6S   4  .System.Windows.Controls.DataGridTemplateColumn  5      $ Delete��6)   $		 120 69   
   CellTemplate
 5      �� 5      .R�5      �� $��Delete��6%   $	��100��66   5      5      5       �� 5!   
   -   5         ��Name$ btnBack��5!      $
��Back��6"   $��50��6H   $��	0 10 0 10q�6S   $��	10 2 10 2q�6f   $��4��6z   $
��Left=�6�   5"      5#      