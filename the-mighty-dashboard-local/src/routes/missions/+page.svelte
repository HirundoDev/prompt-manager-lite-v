<script>
	import { onMount, getContext } from 'svelte';
	import { invoke } from '../../lib/utils/tauri.js';
	import { Play, CheckCircle, Clock, Target, Plus, Search, Filter } from 'lucide-svelte';
	import HelpIcon from '../../lib/components/HelpIcon.svelte';
	import HelpTooltip from '../../lib/components/HelpTooltip.svelte';

	// Contexto de ayuda
	const help = getContext('help');

	let missions = [];
	let loading = true;

	onMount(async () => {
		try {
			missions = [
				{
					id: 'MISSION-001',
					title: 'Implementar autenticación JWT',
					description: 'Configurar sistema de autenticación con tokens JWT',
					status: 'completed',
					priority: 'high',
					session: 'SESSION-001',
					estimatedTime: '2h'
				},
				{
					id: 'MISSION-002',
					title: 'Crear dashboard de métricas',
					description: 'Desarrollar interfaz para visualizar estadísticas',
					status: 'in_progress',
					priority: 'medium',
					session: 'SESSION-002',
					estimatedTime: '3h'
				},
				{
					id: 'MISSION-003',
					title: 'Optimizar queries de base de datos',
					description: 'Mejorar rendimiento de consultas SQL',
					status: 'pending',
					priority: 'low',
					session: null,
					estimatedTime: '1h 30m'
				}
			];
		} catch (error) {
			console.error('Error cargando misiones:', error);
		} finally {
			loading = false;
		}
	});

	function getStatusIcon(status) {
		switch (status) {
			case 'completed': return CheckCircle;
			case 'in_progress': return Play;
			default: return Clock;
		}
	}

	function getStatusColor(status) {
		switch (status) {
			case 'completed': return 'text-green-600 bg-green-100';
			case 'in_progress': return 'text-blue-600 bg-blue-100';
			default: return 'text-gray-600 bg-gray-100';
		}
	}

	function getPriorityColor(priority) {
		switch (priority) {
			case 'high': return 'text-red-600 bg-red-100';
			case 'medium': return 'text-yellow-600 bg-yellow-100';
			default: return 'text-green-600 bg-green-100';
		}
	}
</script>

<div class="p-6">
	<div class="mb-6">
		<h1 class="text-2xl font-bold text-gray-900 dark:text-white flex items-center">
			<Target class="w-6 h-6 mr-2" />
			Misiones
		</h1>
		<p class="text-gray-600 dark:text-gray-400 mt-2">
			Gestiona y rastrea el progreso de tus misiones de desarrollo
		</p>
	</div>

	{#if loading}
		<div class="flex items-center justify-center py-12">
			<div class="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
		</div>
	{:else if missions.length === 0}
		<div class="text-center py-12">
			<Target class="w-12 h-12 text-gray-400 mx-auto mb-4" />
			<h3 class="text-lg font-medium text-gray-900 dark:text-white mb-2">No hay misiones</h3>
			<p class="text-gray-600 dark:text-gray-400">Crea tu primera misión de desarrollo</p>
		</div>
	{:else}
		<div class="grid gap-4">
			{#each missions as mission}
				<div class="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-6">
					<div class="flex items-start justify-between">
						<div class="flex-1">
							<div class="flex items-center mb-2">
								<svelte:component this={getStatusIcon(mission.status)} 
									class="w-5 h-5 mr-2 {getStatusColor(mission.status).split(' ')[0]}" />
								<h3 class="text-lg font-semibold text-gray-900 dark:text-white">
									{mission.title}
								</h3>
							</div>
							<p class="text-gray-600 dark:text-gray-400 mb-3">
								{mission.description}
							</p>
							<div class="flex items-center space-x-4 text-sm">
								<span class="px-2 py-1 text-xs font-medium rounded-full {getPriorityColor(mission.priority)}">
									{mission.priority === 'high' ? 'Alta' : 
									 mission.priority === 'medium' ? 'Media' : 'Baja'} prioridad
								</span>
								<span class="text-gray-500">
									⏱️ {mission.estimatedTime}
								</span>
								{#if mission.session}
									<span class="text-gray-500">
										📋 {mission.session}
									</span>
								{/if}
							</div>
						</div>
						<div class="flex items-center">
							<span class="px-3 py-1 text-sm font-medium rounded-full {getStatusColor(mission.status)}">
								{mission.status === 'completed' ? 'Completada' : 
								 mission.status === 'in_progress' ? 'En progreso' : 'Pendiente'}
							</span>
						</div>
					</div>
				</div>
			{/each}
		</div>
	{/if}
</div>
