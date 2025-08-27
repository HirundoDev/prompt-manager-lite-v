<script>
	import { onMount, getContext } from 'svelte';
	import { invoke } from '../../lib/utils/tauri.js';
	import { BarChart3, Download, Calendar, TrendingUp, Plus, Filter } from 'lucide-svelte';
	import HelpIcon from '../../lib/components/HelpIcon.svelte';
	import HelpTooltip from '../../lib/components/HelpTooltip.svelte';

	// Contexto de ayuda
	const help = getContext('help');

	let stats = {};
	let loading = true;

	onMount(async () => {
		try {
			stats = {
				totalProjects: 2,
				completedMissions: 8,
				totalSessions: 12,
				avgSessionTime: '2h 15m',
				weeklyProgress: [
					{ day: 'Lun', missions: 2 },
					{ day: 'Mar', missions: 3 },
					{ day: 'Mié', missions: 1 },
					{ day: 'Jue', missions: 4 },
					{ day: 'Vie', missions: 2 },
					{ day: 'Sáb', missions: 0 },
					{ day: 'Dom', missions: 1 }
				]
			};
		} catch (error) {
			console.error('Error cargando reportes:', error);
		} finally {
			loading = false;
		}
	});
</script>

<div class="p-6">
	<div class="mb-6 flex items-center justify-between">
		<div>
			<h1 class="text-2xl font-bold text-gray-900 dark:text-white flex items-center">
				<BarChart3 class="w-6 h-6 mr-2" />
				Reportes y Métricas
			</h1>
			<p class="text-gray-600 dark:text-gray-400 mt-2">
				Analiza tu productividad y rendimiento
			</p>
		</div>
		
		<div class="flex items-center space-x-3">
			<div class="flex items-center space-x-1">
				<button class="mighty-button-secondary">
					<Download class="w-4 h-4 mr-2" />
					Exportar
				</button>
				<HelpTooltip text={help.getTooltipText('reports.export')}>
					<HelpIcon helpKey="reports.export" variant="modal" size="sm" on:help={(e) => help.showModal(e.detail.helpKey)} />
				</HelpTooltip>
			</div>
			
			<div class="flex items-center space-x-1">
				<button class="mighty-button-primary">
					<Plus class="w-4 h-4 mr-2" />
					Generar Reporte
				</button>
				<HelpTooltip text={help.getTooltipText('reports.generate')}>
					<HelpIcon helpKey="reports.generate" variant="modal" size="sm" on:help={(e) => help.showModal(e.detail.helpKey)} />
				</HelpTooltip>
			</div>
		</div>
	</div>

	{#if loading}
		<div class="flex items-center justify-center py-12">
			<div class="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
		</div>
	{:else}
		<!-- Métricas principales -->
		<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
			<div class="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-6">
				<div class="flex items-center">
					<div class="p-2 bg-blue-100 rounded-lg">
						<BarChart3 class="w-6 h-6 text-blue-600" />
					</div>
					<div class="ml-4">
						<p class="text-sm font-medium text-gray-600 dark:text-gray-400">Proyectos Totales</p>
						<p class="text-2xl font-bold text-gray-900 dark:text-white">{stats.totalProjects}</p>
					</div>
				</div>
			</div>

			<div class="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-6">
				<div class="flex items-center">
					<div class="p-2 bg-green-100 rounded-lg">
						<TrendingUp class="w-6 h-6 text-green-600" />
					</div>
					<div class="ml-4">
						<p class="text-sm font-medium text-gray-600 dark:text-gray-400">Misiones Completadas</p>
						<p class="text-2xl font-bold text-gray-900 dark:text-white">{stats.completedMissions}</p>
					</div>
				</div>
			</div>

			<div class="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-6">
				<div class="flex items-center">
					<div class="p-2 bg-purple-100 rounded-lg">
						<Calendar class="w-6 h-6 text-purple-600" />
					</div>
					<div class="ml-4">
						<p class="text-sm font-medium text-gray-600 dark:text-gray-400">Sesiones Totales</p>
						<p class="text-2xl font-bold text-gray-900 dark:text-white">{stats.totalSessions}</p>
					</div>
				</div>
			</div>

			<div class="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-6">
				<div class="flex items-center">
					<div class="p-2 bg-orange-100 rounded-lg">
						<TrendingUp class="w-6 h-6 text-orange-600" />
					</div>
					<div class="ml-4">
						<p class="text-sm font-medium text-gray-600 dark:text-gray-400">Tiempo Promedio</p>
						<p class="text-2xl font-bold text-gray-900 dark:text-white">{stats.avgSessionTime}</p>
					</div>
				</div>
			</div>
		</div>

		<!-- Gráfico de progreso semanal -->
		<div class="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-6 mb-8">
			<h2 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">Progreso Semanal</h2>
			<div class="flex items-end space-x-2 h-32">
				{#each stats.weeklyProgress as day}
					<div class="flex-1 flex flex-col items-center">
						<div class="w-full bg-primary-500 rounded-t" style="height: {(day.missions / 4) * 100}%"></div>
						<span class="text-xs text-gray-600 dark:text-gray-400 mt-2">{day.day}</span>
						<span class="text-xs font-medium text-gray-900 dark:text-white">{day.missions}</span>
					</div>
				{/each}
			</div>
		</div>

		<!-- Acciones de exportación -->
		<div class="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-6">
			<h2 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">Exportar Datos</h2>
			<div class="flex space-x-4">
				<button class="flex items-center px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors">
					<Download class="w-4 h-4 mr-2" />
					Exportar CSV
				</button>
				<button class="flex items-center px-4 py-2 bg-gray-600 text-white rounded-lg hover:bg-gray-700 transition-colors">
					<Download class="w-4 h-4 mr-2" />
					Exportar PDF
				</button>
			</div>
		</div>
	{/if}
</div>
