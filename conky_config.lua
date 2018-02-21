conky.config = {
	-- Window Configurations
	border_width = 0,
    own_window = true,
    own_window_class = 'Conky',
    own_window_type = 'dock',
    own_window_hints = 'undecorated,below,sticky,skip_taskbar,skip_pager',
    own_window_transparent = false,
    own_window_argb_visual = true,
    own_window_argb_value = 128,
    own_window_colour = '000000',
	minimum_height = 300,
	maximum_width = 300,
	alignment = 'top_right',
	gap_x = 12,
	gap_y = 35,
	background = false,

	-- System Configurations
    double_buffer = true,
    cpu_avg_samples = 1,
	update_interval = 1,
	total_run_times = 0,
	no_buffers = true,
	override_utf8_locale = true,

	-- Styling Configurations
	use_xft = true,
	font = 'Roboto:size=7',
	default_color = white,
	default_shade_color = black,
	default_bar_height = 3,
	default_graph_height = 20,
	draw_borders = false,
    draw_graph_borders = true,
    draw_outline = false,
    draw_shades = false,
	stippled_borders = 0,
	uppercase = true,
	short_units = true,
}

conky.text = [[
	${execpi 1 ~/.conky/conky.py} # Run the conky Script
]]
