conky.config = {
	-- Window Configurations
	border_width = 0,
    own_window = true,
    own_window_class = 'Conky',
    own_window_type = 'desktop',
    own_window_hints = 'undecorated,below,sticky,skip_taskbar,skip_pager',
    own_window_transparent = false,
    own_window_argb_visual = true,
    own_window_argb_value = 192,
    own_window_colour = '000000',
    double_buffer = true,
    background = true,
    stippled_borders = 0,

	-- Window Position
	minimum_height = 300,
	maximum_width = 300,

	alignment = 'top_right',
	gap_x = 12,
	gap_y = 35,

	background = false,
	cpu_avg_samples = 2,
	default_color = white,
	default_shade_color = black,
	draw_borders = false,
    draw_graph_borders = true,
    draw_outline = false,
    draw_shades = false,
	use_xft = true,
	font = 'Roboto:size=7',

	update_interval = 1,
	total_run_times = 0,


	
	default_bar_height = 3,
	default_graph_height = 20,

	no_buffers = true,
	
	override_utf8_locale = true,
	uppercase = true,
	short_units = true,
}

conky.text = [[
# Run the conky Script
# Pass the network interface name as a parameter
${execpi 1 /home/matt/.conky/conky.py enx00e04c36010c}
]]