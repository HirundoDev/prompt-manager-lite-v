<script>
	import { onMount, getContext } from 'svelte';
	import { invoke } from '../../lib/utils/tauri.js';
	import { FileText, Play, Clock, Calendar, Plus, Search, Filter } from 'lucide-svelte';
	import HelpIcon from '../../lib/components/HelpIcon.svelte';
	import HelpTooltip from '../../lib/components/HelpTooltip.svelte';

	// Contexto de ayuda
	const help = getContext('help');

	let sessions = [];
	let loading = true;

	onMount(async () => {
		try {
			// Cargar sesiones desde el backend
			sessions = [
				{
					id: 'SESSION-001',
					name: 'Backend API Setup',
					date: '2025-08-27',
					status: 'completed',
					duration: '2h 30m',
					missions: 5
				},
				{
					id: 'SESSION-002', 
					name: 'Frontend Dashboard',
					date: '2025-08-26',
					status: 'in_progress',
					duration: '1h 45m',
					missions: 3
				}
			];
		} catch (error) {
			console.error('Error cargando sesiones:', error);
		} finally {
			loading = false;
		}
	});

	function getStatusColor(status) {
		switch (status) {
			case 'completed': return 'bg-green-100 text-green-800';
			case 'in_progress': return 'bg-blue-100 text-blue-800';
			case 'pending': return 'bg-gray-100 text-gray-800';
			default: return 'bg-gray-100 text-gray-800';
		}
	}
</script>

<div class="p-6">
	<div class="mb-6 flex items-center justify-between">
		<div>
			<h1 class="text-2xl font-bold text-gray-900 dark:text-white flex items-center">
				<FileText class="w-6 h-6 mr-2" />
				Sesiones de Trabajo
			</h1>
			<p class="text-gray-600 dark:text-gray-400 mt-2">
				Gestiona y revisa tus sesiones de trabajo diarias
			</p>
		</div>
		
		<div class="flex items-center space-x-3">
			<div class="flex items-center space-x-1">
				<button class="mighty-button-secondary">
					<Search class="w-4 h-4 mr-2" />
					Buscar
				</button>
				<HelpTooltip text={help.getTooltipText('sessions.search')}>
					<HelpIcon helpKey="sessions.search" variant="modal" size="sm" on:help={(e) => help.showModal(e.detail.helpKey)} />
				</HelpTooltip>
			</div>
			
			<div class="flex items-center space-x-1">
				<button class="mighty-button-secondary">
					<Filter class="w-4 h-4 mr-2" />
					Filtros
				</button>
				<HelpTooltip text={help.getTooltipText('sessions.filters')}>
					<HelpIcon helpKey="sessions.filters" variant="modal" size="sm" on:help={(e) => help.showModal(e.detail.helpKey)} />
				</HelpTooltip>
			</div>
			
			<div class="flex items-center space-x-1">
				<button class="mighty-button-primary">
					<Plus class="w-4 h-4 mr-2" />
					Nueva Sesión
				</button>
				<HelpTooltip text={help.getTooltipText('sessions.create')}>
					<HelpIcon helpKey="sessions.create" variant="modal" size="sm" on:help={(e) => help.showModal(e.detail.helpKey)} />
				</HelpTooltip>
			</div>
		</div>
	</div>

	{#if loading}
		<div class="flex items-center justify-center py-12">
			<div class="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
		</div>
	{:else if sessions.length === 0}
		<div class="text-center py-12">
			<FileText class="w-12 h-12 text-gray-400 mx-auto mb-4" />
			<h3 class="text-lg font-medium text-gray-900 dark:text-white mb-2">No hay sesiones</h3>
			<p class="text-gray-600 dark:text-gray-400">Crea tu primera sesión de trabajo</p>
		</div>
	{:else}
		<div class="grid gap-4">
			{#each sessions as session}
				<div class="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-6">
					<div class="flex items-start justify-between">
						<div class="flex-1">
							<h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">
								{session.name}
							</h3>
							<div class="flex items-center space-x-4 text-sm text-gray-600 dark:text-gray-400">
								<div class="flex items-center">
									<Calendar class="w-4 h-4 mr-1" />
									{session.date}
								</div>
								<div class="flex items-center">
									<Clock class="w-4 h-4 mr-1" />
									{session.duration}
								</div>
								<div class="flex items-center">
									<Play class="w-4 h-4 mr-1" />
									{session.missions} misiones
								</div>
							</div>
						</div>
						<div class="flex items-center space-x-2">
							<span class="px-2 py-1 text-xs font-medium rounded-full {getStatusColor(session.status)}">
								{session.status === 'completed' ? 'Completada' : 
								 session.status === 'in_progress' ? 'En progreso' : 'Pendiente'}
							</span>
						</div>
					</div>
				</div>
			{/each}
		</div>
	{/if}
</div>
